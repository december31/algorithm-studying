from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.user_progress import UserProgress
from app.schemas.user_progress import UserProgressResponse, UserProgressUpdate

router = APIRouter()


@router.get("/{user_handle}", response_model=UserProgressResponse)
async def get_or_create_user_progress(
    user_handle: str,
    db: AsyncSession = Depends(get_db),
):
    """Retrieve player level, floor, XP, and completed problems."""
    stmt = select(UserProgress).where(UserProgress.user_handle == user_handle)
    result = await db.execute(stmt)
    progress = result.scalar_one_or_none()

    if not progress:
        progress = UserProgress(
            user_handle=user_handle,
            level=1,
            xp=0,
            dungeon_floor=1,
            completed_problems=[],
        )
        db.add(progress)
        await db.commit()
        await db.refresh(progress)

    return progress


@router.post("/{user_handle}", response_model=UserProgressResponse)
async def update_user_progress(
    user_handle: str,
    payload: UserProgressUpdate,
    db: AsyncSession = Depends(get_db),
):
    """Update player level, floor, XP, or record completed problems."""
    stmt = select(UserProgress).where(UserProgress.user_handle == user_handle)
    result = await db.execute(stmt)
    progress = result.scalar_one_or_none()

    if not progress:
        progress = UserProgress(
            user_handle=user_handle,
            level=1,
            xp=0,
            dungeon_floor=1,
            completed_problems=[],
        )
        db.add(progress)

    if payload.xp_gained:
        progress.xp += payload.xp_gained
    if payload.level is not None:
        progress.level = payload.level
    if payload.dungeon_floor is not None:
        progress.dungeon_floor = payload.dungeon_floor
    if payload.completed_problem_id:
        completed = list(progress.completed_problems or [])
        if payload.completed_problem_id not in completed:
            completed.append(payload.completed_problem_id)
            progress.completed_problems = completed

    await db.commit()
    await db.refresh(progress)
    return progress
