from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class HeroSignUp(BaseModel):
    """Sign up using a legendary adventurer name and secret incantation (password)."""
    hero_name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Your adventurer / player call-sign (username)",
    )
    secret_incantation: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Your secret incantation / spell (password)",
    )


class HeroLogin(BaseModel):
    """Log in to access your adventurer stats and passed problem records."""
    hero_name: str = Field(..., description="Adventurer call-sign")
    secret_incantation: str = Field(..., description="Secret incantation (password)")


class HeroProfile(BaseModel):
    id: int
    hero_name: str
    level: int
    xp: int
    dungeon_floor: int
    passed_problems: List[str]
    token: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class MarkProblemPassed(BaseModel):
    problem_id: str = Field(..., description="The ID of the problem to mark as conquered / passed")


class PassedProblemsResponse(BaseModel):
    hero_name: str
    passed_problems: List[str]
    total_passed: int
