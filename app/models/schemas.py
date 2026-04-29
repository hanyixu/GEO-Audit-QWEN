from typing import List, Optional

from pydantic import BaseModel, Field


class AuditRequest(BaseModel):
    content: str = Field(..., min_length=1, description="Content to audit")
    focus_areas: Optional[List[str]] = Field(
        default=None,
        description="Optional list of GEO skills to focus on",
    )


class AuditResponse(BaseModel):
    result: str
    used_focus_areas: List[str]
