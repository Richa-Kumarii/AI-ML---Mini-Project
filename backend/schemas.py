from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class GenerateRequest(BaseModel):
    topic: str = Field(..., min_length=2, max_length=500, description="Central topic or creative concept")
    description: Optional[str] = Field(None, max_length=2000, description="Optional extra background or context")
    platforms: List[str] = Field(..., min_items=1, description="Selected social media platforms")
    target_audience: Optional[str] = Field("General Audience", max_length=200)
    language: str = Field("English", description="English, Hindi, or Hinglish")
    tone: str = Field("Motivational", description="Content tone")
    content_type: str = Field("Post", description="Preferred general format")
    length: str = Field("Medium", description="Short, Medium, or Long")
    keywords: Optional[List[str]] = Field(default_factory=list)
    custom_instructions: Optional[str] = Field(None, max_length=1000)

class PlatformResult(BaseModel):
    platform: str
    title: Optional[str] = None
    hook: Optional[str] = None
    main_content: str
    call_to_action: Optional[str] = None
    hashtags: List[str] = Field(default_factory=list)
    content_type: str
    word_count: int
    character_count: int
    is_valid: bool
    validation_warnings: List[str] = Field(default_factory=list)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class GenerateResponse(BaseModel):
    id: Optional[int] = None
    topic: str
    results: Dict[str, PlatformResult]
    created_at: Optional[str] = None

class RegenerateRequest(BaseModel):
    generation_id: Optional[int] = None
    platform: str
    topic: str
    description: Optional[str] = None
    target_audience: Optional[str] = "General Audience"
    language: str = "English"
    tone: str = "Motivational"
    content_type: str = "Post"
    length: str = "Medium"
    keywords: Optional[List[str]] = Field(default_factory=list)
    custom_instructions: Optional[str] = None

class RewriteRequest(BaseModel):
    platform: str
    topic: str
    current_content: str
    instruction: str = Field(..., description="E.g., 'Make it funnier', 'Make it shorter', 'Translate to Hinglish'")
    target_audience: Optional[str] = "General Audience"
    language: Optional[str] = None
    tone: Optional[str] = None
    length: Optional[str] = None

class HistoryItemResponse(BaseModel):
    id: int
    topic: str
    description: Optional[str]
    selected_platforms: List[str]
    target_audience: Optional[str]
    language: str
    tone: str
    content_type: str
    length: str
    keywords: Optional[List[str]]
    results: Dict[str, Any]
    created_at: str

