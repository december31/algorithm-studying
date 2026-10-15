from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.submission import Submission
from app.schemas.submission import SubmissionCreate, SubmissionResponse

router = APIRouter()


@router.post("", response_model=SubmissionResponse, status_code=status.HTTP_201_CREATED)
async def create_submission(
    payload: SubmissionCreate,
    db: AsyncSession = Depends(get_db),
):
    """Save a problem submission result."""
    submission = Submission(
        problem_id=payload.problem_id,
        language=payload.language,
        code=payload.code,
        status=payload.status,
        tests_passed=payload.tests_passed,
        total_tests=payload.total_tests,
        execution_time_ms=payload.execution_time_ms,
    )
    db.add(submission)
    await db.commit()
    await db.refresh(submission)
    return submission


@router.get("", response_model=List[SubmissionResponse])
async def list_submissions(
    problem_id: Optional[str] = Query(None, description="Filter submissions by problem ID"),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    """List recent submissions with pagination and optional problem filter."""
    stmt = select(Submission).order_by(desc(Submission.created_at)).offset(offset).limit(limit)
    if problem_id:
        stmt = stmt.where(Submission.problem_id == problem_id)

    result = await db.execute(stmt)
    return result.scalars().all()


@router.get("/{submission_id}", response_model=SubmissionResponse)
async def get_submission(
    submission_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Fetch details of a single submission."""
    stmt = select(Submission).where(Submission.id == submission_id)
    result = await db.execute(stmt)
    submission = result.scalar_one_or_none()
    if not submission:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Submission with ID {submission_id} not found",
        )
    return submission
