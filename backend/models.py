from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from datetime import datetime
from database import Base

class ContentGeneration(Base):
    __tablename__ = "content_generations"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String(500), nullable=False, index=True)
    description = Column(Text, nullable=True)
    selected_platforms = Column(JSON, nullable=False)  # List of strings e.g. ["instagram", "youtube"]
    target_audience = Column(String(200), nullable=True)
    language = Column(String(50), nullable=False, default="English")
    tone = Column(String(50), nullable=False, default="Engaging")
    content_type = Column(String(100), nullable=False, default="Post")
    length = Column(String(50), nullable=False, default="Medium")
    keywords = Column(JSON, nullable=True)  # List of string keywords
    custom_instructions = Column(Text, nullable=True)
    
    # Stores the generated dictionary of results per platform
    results = Column(JSON, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "topic": self.topic,
            "description": self.description,
            "selected_platforms": self.selected_platforms,
            "target_audience": self.target_audience,
            "language": self.language,
            "tone": self.tone,
            "content_type": self.content_type,
            "length": self.length,
            "keywords": self.keywords,
            "custom_instructions": self.custom_instructions,
            "results": self.results,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

