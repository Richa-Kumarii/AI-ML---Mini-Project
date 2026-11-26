"""
FastAPI Main Application.
Provides RESTful endpoints for multi-platform generation, regeneration, rewrites, and history.
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Dict, Any
import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()

from database import engine, Base, get_db
from models import ContentGeneration
from schemas import (
    GenerateRequest,
    GenerateResponse,
    RegenerateRequest,
    RewriteRequest,
    PlatformResult,
    HistoryItemResponse
)
from content_generator import ContentGenerator
from history_service import HistoryService
from nvidia_service import nvidia_service
from platform_config import PLATFORM_CONFIG, VALID_TONES, VALID_LANGUAGES, VALID_LENGTHS

# Initialize SQLite database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI-Powered Smart Multi-Platform Content Generator",
    description="Entertainment Content Generator converting 1 Topic into optimized outputs for Instagram, YouTube, Shorts, Facebook, X, & LinkedIn",
    version="1.0.0"
)

# CORS configuration
origins_str = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173")
origins = [origin.strip() for origin in origins_str.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "nvidia_configured": nvidia_service.is_configured(),
        "primary_model": nvidia_service.primary_model,
        "fallback_model": nvidia_service.fallback_model
    }

@app.get("/api/config")
def get_configuration():
    """Returns platform metadata, rules, available tones, and languages for frontend rendering."""
    return {
        "platforms": PLATFORM_CONFIG,
        "tones": VALID_TONES,
        "languages": VALID_LANGUAGES,
        "lengths": VALID_LENGTHS
    }

@app.post("/api/generate", response_model=GenerateResponse)
def generate_content(req: GenerateRequest, db: Session = Depends(get_db)):
    try:
        results = ContentGenerator.generate_all(req)
        # Automatically save generation run to SQLite database
        saved_entry = HistoryService.save_generation(db, req, results)
        return GenerateResponse(
            id=saved_entry.id,
            topic=saved_entry.topic,
            results=results,
            created_at=saved_entry.created_at.isoformat() if saved_entry.created_at else None
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/regenerate", response_model=PlatformResult)
def regenerate_platform_content(req: RegenerateRequest, db: Session = Depends(get_db)):
    try:
        result = ContentGenerator.generate_for_platform(
            platform=req.platform.lower(),
            topic=req.topic,
            description=req.description,
            target_audience=req.target_audience,
            language=req.language,
            tone=req.tone,
            content_type=req.content_type,
            length=req.length,
            keywords=req.keywords,
            custom_instructions=req.custom_instructions
        )
        
        # If generation_id is provided, optionally update history entry
        if req.generation_id:
            entry = HistoryService.get_by_id(db, req.generation_id)
            if entry and isinstance(entry.results, dict):
                current_results = dict(entry.results)
                current_results[req.platform.lower()] = result.dict()
                entry.results = current_results
                db.commit()
                
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/rewrite", response_model=PlatformResult)
def rewrite_platform_content(req: RewriteRequest):
    try:
        result = ContentGenerator.rewrite_content(req)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/history", response_model=List[HistoryItemResponse])
def get_history(limit: int = 50, skip: int = 0, db: Session = Depends(get_db)):
    items = HistoryService.get_all(db, limit=limit, skip=skip)
    return [
        HistoryItemResponse(
            id=item.id,
            topic=item.topic,
            description=item.description,
            selected_platforms=item.selected_platforms,
            target_audience=item.target_audience,
            language=item.language,
            tone=item.tone,
            content_type=item.content_type,
            length=item.length,
            keywords=item.keywords or [],
            results=item.results,
            created_at=item.created_at.isoformat() if item.created_at else ""
        )
        for item in items
    ]

@app.get("/api/history/{entry_id}", response_model=HistoryItemResponse)
def get_history_entry(entry_id: int, db: Session = Depends(get_db)):
    item = HistoryService.get_by_id(db, entry_id)
    if not item:
        raise HTTPException(status_code=404, detail="Generation history entry not found.")
    return HistoryItemResponse(
        id=item.id,
        topic=item.topic,
        description=item.description,
        selected_platforms=item.selected_platforms,
        target_audience=item.target_audience,
        language=item.language,
        tone=item.tone,
        content_type=item.content_type,
        length=item.length,
        keywords=item.keywords or [],
        results=item.results,
        created_at=item.created_at.isoformat() if item.created_at else ""
    )

@app.delete("/api/history/{entry_id}")
def delete_history_entry(entry_id: int, db: Session = Depends(get_db)):
    success = HistoryService.delete_by_id(db, entry_id)
    if not success:
        raise HTTPException(status_code=404, detail="Entry not found or already deleted.")
    return {"message": f"Successfully deleted history item {entry_id}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

