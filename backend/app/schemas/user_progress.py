from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class UserProgressUpdate(BaseModel):
    xp_gained: Optional[int] = Field(default=0, ge=0)
    level: Optional[int] = Field(default=None, ge=1)
    dungeon_floor: Optional[int] = Field(default=None, ge=1)
    completed_problem_id: Optional[str] = None


class UserProgressResponse(BaseModel):
    id: int
    user_handle: str
    level: int
    xp: int
    dungeon_floor: int
    completed_problems: List[str]
    updated_at: datetime

    class Config:
        from_attributes = True
