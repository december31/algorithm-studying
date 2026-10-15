from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.problem import Problem
from app.schemas.problem import ProblemDetailResponse, ProblemSummary

router = APIRouter()


@router.get("", response_model=List[ProblemSummary])
async def list_problems(
    wing_id: Optional[str] = Query(None, description="Filter by wing/topic"),
    difficulty: Optional[str] = Query(None, description="Filter by difficulty: easy, medium, hard"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
) -> Any:
    """Retrieve catalog of algorithm challenges."""
    query = select(Problem)
    if wing_id:
        query = query.where(Problem.wing_id == wing_id)
    if difficulty:
        query = query.where(Problem.difficulty == difficulty)
    
    query = query.order_by(Problem.wing_id, Problem.floor).offset(offset).limit(limit)
    result = await db.execute(query)
    problems = result.scalars().all()

    return [
        ProblemSummary(
            id=p.id,
            wingId=p.wing_id,
            floor=p.floor,
            title=p.title,
            difficulty=p.difficulty,
            visualizerType=p.visualizer_type,
            leetcodeId=p.leetcode_id,
            leetcodeTitle=p.leetcode_title,
            leetcodeUrl=p.leetcode_url,
            monster=p.monster,
        )
        for p in problems
    ]


@router.get("/catalog/summary")
async def get_full_catalog(db: AsyncSession = Depends(get_db)) -> Any:
    """Get complete lightweight catalog for client-side dungeon generation."""
    query = select(Problem).order_by(Problem.wing_id, Problem.floor)
    result = await db.execute(query)
    problems = result.scalars().all()

    return [
        {
            "id": p.id,
            "wingId": p.wing_id,
            "floor": p.floor,
            "title": p.title,
            "difficulty": p.difficulty,
            "visualizerType": p.visualizer_type,
            "leetcodeId": p.leetcode_id,
            "leetcodeTitle": p.leetcode_title,
            "leetcodeUrl": p.leetcode_url,
            "monster": p.monster,
        }
        for p in problems
    ]


@router.get("/stats")
async def get_problem_stats(db: AsyncSession = Depends(get_db)) -> Any:
    """Get problem counts by wing and difficulty."""
    total = await db.scalar(select(func.count()).select_from(Problem)) or 0
    
    # By difficulty
    diff_query = select(Problem.difficulty, func.count()).group_by(Problem.difficulty)
    diff_res = await db.execute(diff_query)
    diff_counts = dict(diff_res.all())

    # By wing
    wing_query = select(Problem.wing_id, func.count()).group_by(Problem.wing_id)
    wing_res = await db.execute(wing_query)
    wing_counts = dict(wing_res.all())

    return {
        "total": total,
        "by_difficulty": diff_counts,
        "by_wing": wing_counts,
    }


@router.get("/{problem_id}", response_model=ProblemDetailResponse)
async def get_problem(problem_id: str, db: AsyncSession = Depends(get_db)) -> Any:
    """Get full problem details including description, test cases, hints, and Python code."""
    result = await db.execute(select(Problem).where(Problem.id == problem_id))
    problem = result.scalar_one_or_none()

    if not problem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Problem '{problem_id}' not found",
        )

    return ProblemDetailResponse(
        id=problem.id,
        wingId=problem.wing_id,
        floor=problem.floor,
        title=problem.title,
        difficulty=problem.difficulty,
        visualizerType=problem.visualizer_type,
        monster=problem.monster,
        description=problem.description,
        examples=problem.examples,
        constraints=problem.constraints,
        starterCode=problem.starter_code,
        solutionCode=problem.solution_code,
        functionName=problem.function_name,
        testCases=problem.test_cases,
        hints=problem.hints,
        python=problem.python,
        leetcodeId=problem.leetcode_id,
        leetcodeTitle=problem.leetcode_title,
        leetcodeUrl=problem.leetcode_url,
        created_at=problem.created_at,
        updated_at=problem.updated_at,
    )
