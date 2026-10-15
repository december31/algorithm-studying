from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class MonsterSchema(BaseModel):
    id: str
    name: str
    title: str
    maxHp: int
    hp: int
    sprite: str
    color: str
    attackName: str
    attackPower: int
    defeatQuote: str


class ProblemBase(BaseModel):
    id: str
    wingId: str
    floor: int = 1
    title: str
    difficulty: str
    visualizerType: str = "array"
    monster: Dict[str, Any] = Field(default_factory=dict)
    description: str = ""
    examples: List[Dict[str, Any]] = Field(default_factory=list)
    constraints: List[str] = Field(default_factory=list)
    starterCode: str = ""
    solutionCode: str = ""
    functionName: str = "solution"
    testCases: List[Dict[str, Any]] = Field(default_factory=list)
    hints: List[str] = Field(default_factory=list)
    python: Dict[str, Any] = Field(default_factory=dict)
    leetcodeId: Optional[int] = None
    leetcodeTitle: Optional[str] = None
    leetcodeUrl: Optional[str] = None


class ProblemSummary(BaseModel):
    id: str
    wingId: str
    floor: int
    title: str
    difficulty: str
    visualizerType: str
    leetcodeId: Optional[int] = None
    leetcodeTitle: Optional[str] = None
    leetcodeUrl: Optional[str] = None
    monster: Dict[str, Any]


class ProblemDetailResponse(ProblemBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
