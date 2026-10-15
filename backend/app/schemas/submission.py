from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class SubmissionCreate(BaseModel):
    problem_id: str = Field(..., max_length=100, description="Unique identifier of the problem")
    language: str = Field(..., max_length=50, description="Programming language (e.g. python, javascript)")
    code: str = Field(..., description="Source code submitted by the user")
    status: str = Field(default="ACCEPTED", max_length=50, description="Result status")
    tests_passed: int = Field(default=0, ge=0)
    total_tests: int = Field(default=0, ge=0)
    execution_time_ms: Optional[float] = Field(default=None, description="Execution time in milliseconds")


class SubmissionResponse(BaseModel):
    id: int
    problem_id: str
    language: str
    code: str
    status: str
    tests_passed: int
    total_tests: int
    execution_time_ms: Optional[float]
    created_at: datetime

    class Config:
        from_attributes = True
