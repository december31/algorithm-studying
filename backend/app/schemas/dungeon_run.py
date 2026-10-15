from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel, Field


class DungeonRunSave(BaseModel):
    wing_id: str = Field(..., max_length=50)
    current_floor: int = Field(default=1, ge=1, le=10)
    max_floor_reached: Optional[int] = Field(default=1, ge=1, le=10)
    status: Optional[str] = Field(default="in_progress")
    run_catalog: List[Any] = Field(default_factory=list)
    current_problem_id: str = Field(...)
    code: Optional[str] = Field(default="")
    language: Optional[str] = Field(default="python")
    hp: Optional[int] = Field(default=100)
    max_hp: Optional[int] = Field(default=100)
    gold: Optional[int] = Field(default=50)
    potions: Optional[int] = Field(default=2)


class DungeonRunResponse(BaseModel):
    id: int
    hero_name: str
    wing_id: str
    current_floor: int
    max_floor_reached: int
    status: str
    run_catalog: List[Any]
    current_problem_id: str
    code: str
    language: str
    hp: int
    max_hp: int
    gold: int
    potions: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
