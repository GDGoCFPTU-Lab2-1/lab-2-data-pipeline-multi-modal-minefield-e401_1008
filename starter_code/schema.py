from pydantic import BaseModel, Field
<<<<<<< HEAD
from typing import Optional, List, Any
=======
from typing import Optional, List
>>>>>>> origin/main
from datetime import datetime

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================
# Your task is to define the Unified Schema for all sources.
# This is v1. Note: A breaking change is coming at 11:00 AM!

class UnifiedDocument(BaseModel):
<<<<<<< HEAD
    """
    Unified Schema v1 for multi-source ingestion.
    Supports PDF, Transcript, HTML, CSV, and Legacy Code.
    """
    document_id: str = Field(..., description="Unique identifier for the document")
    content: str = Field(..., description="Main text content or extracted summary")
    source_type: str = Field(..., description="Source format: PDF, Transcript, HTML, CSV, or Code")
    author: Optional[str] = Field("Unknown", description="Author of the source document")
    timestamp: Optional[datetime] = Field(None, description="Extraction or creation timestamp")
    
    # Flexible metadata field for source-specific attributes (e.g., tables, speaker labels)
    source_metadata: dict[str, Any] = Field(default_factory=dict)

    class Config:
        json_schema_extra = {
            "example": {
                "document_id": "csv_pdf_001",
                "content": "Sample content...",
                "source_type": "PDF",
                "author": "Dr. Smith",
                "timestamp": "2024-04-24T10:00:00",
                "source_metadata": {"tables_found": 2}
            }
        }
=======
    # TODO: Define the v1 schema. 
    # Suggested fields: document_id, content, source_type, author, timestamp, metadata
    
    document_id: str
    content: str
    source_type: str # e.g., 'PDF', 'Video', 'HTML', 'CSV', 'Code'
    author: Optional[str] = "Unknown"
    timestamp: Optional[datetime] = None
    
    # You might want a dict for source-specific metadata
    source_metadata: dict = Field(default_factory=dict)
>>>>>>> origin/main
