"""
History Service.
Handles saving, querying, and deleting generation runs using SQLAlchemy and SQLite.
"""

from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from models import ContentGeneration
from schemas import GenerateRequest, PlatformResult

class HistoryService:
    @staticmethod
    def save_generation(
        db: Session,
        req: GenerateRequest,
        results: Dict[str, PlatformResult]
    ) -> ContentGeneration:
        results_dict = {k: v.dict() for k, v in results.items()}
        entry = ContentGeneration(
            topic=req.topic,
            description=req.description,
            selected_platforms=req.platforms,
            target_audience=req.target_audience,
            language=req.language,
            tone=req.tone,
            content_type=req.content_type,
            length=req.length,
            keywords=req.keywords,
            custom_instructions=req.custom_instructions,
            results=results_dict
        )
        db.add(entry)
        db.commit()
        db.refresh(entry)
        return entry

    @staticmethod
    def get_all(db: Session, limit: int = 50, skip: int = 0) -> List[ContentGeneration]:
        return db.query(ContentGeneration).order_by(ContentGeneration.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, entry_id: int) -> Optional[ContentGeneration]:
        return db.query(ContentGeneration).filter(ContentGeneration.id == entry_id).first()

    @staticmethod
    def delete_by_id(db: Session, entry_id: int) -> bool:
        entry = db.query(ContentGeneration).filter(ContentGeneration.id == entry_id).first()
        if entry:
            db.delete(entry)
            db.commit()
            return True
        return False

