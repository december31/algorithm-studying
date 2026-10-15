from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.endpoints.auth import get_current_hero
from app.core.database import get_db
from app.models.dungeon_run import DungeonRun
from app.models.user import User
from app.schemas.dungeon_run import DungeonRunResponse, DungeonRunSave

router = APIRouter()


@router.post("/runs", response_model=DungeonRunResponse)
async def save_or_update_dungeon_run(
    payload: DungeonRunSave,
    current_hero: User = Depends(get_current_hero),
    db: AsyncSession = Depends(get_db),
):
    """Save or update the in-progress state of a dungeon run."""
    stmt = (
        select(DungeonRun)
        .where(
            DungeonRun.hero_name == current_hero.hero_name,
            DungeonRun.wing_id == payload.wing_id,
            DungeonRun.status == "in_progress",
        )
        .order_by(desc(DungeonRun.updated_at))
    )
    result = await db.execute(stmt)
    existing_run = result.scalar_one_or_none()

    max_floor = max(payload.current_floor, payload.max_floor_reached or payload.current_floor)

    if existing_run:
        existing_run.current_floor = payload.current_floor
        existing_run.max_floor_reached = max(existing_run.max_floor_reached, max_floor)
        existing_run.status = payload.status or "in_progress"
        existing_run.run_catalog = payload.run_catalog
        existing_run.current_problem_id = payload.current_problem_id
        if payload.code is not None:
            existing_run.code = payload.code
        if payload.language:
            existing_run.language = payload.language
        if payload.hp is not None:
            existing_run.hp = payload.hp
        if payload.max_hp is not None:
            existing_run.max_hp = payload.max_hp
        if payload.gold is not None:
            existing_run.gold = payload.gold
        if payload.potions is not None:
            existing_run.potions = payload.potions
        run_record = existing_run
    else:
        run_record = DungeonRun(
            hero_name=current_hero.hero_name,
            wing_id=payload.wing_id,
            current_floor=payload.current_floor,
            max_floor_reached=max_floor,
            status=payload.status or "in_progress",
            run_catalog=payload.run_catalog,
            current_problem_id=payload.current_problem_id,
            code=payload.code or "",
            language=payload.language or "python",
            hp=payload.hp if payload.hp is not None else 100,
            max_hp=payload.max_hp if payload.max_hp is not None else 100,
            gold=payload.gold if payload.gold is not None else 50,
            potions=payload.potions if payload.potions is not None else 2,
        )
        db.add(run_record)

    await db.commit()
    await db.refresh(run_record)
    return run_record


@router.get("/runs", response_model=List[DungeonRunResponse])
async def list_active_dungeon_runs(
    current_hero: User = Depends(get_current_hero),
    db: AsyncSession = Depends(get_db),
):
    """Retrieve all running/in-progress dungeons for this hero."""
    stmt = (
        select(DungeonRun)
        .where(
            DungeonRun.hero_name == current_hero.hero_name,
            DungeonRun.status == "in_progress",
        )
        .order_by(desc(DungeonRun.updated_at))
    )
    result = await db.execute(stmt)
    return result.scalars().all()


@router.get("/runs/{wing_id}", response_model=DungeonRunResponse)
async def get_active_dungeon_run_by_wing(
    wing_id: str,
    current_hero: User = Depends(get_current_hero),
    db: AsyncSession = Depends(get_db),
):
    """Retrieve the active running dungeon for a specific wing."""
    stmt = (
        select(DungeonRun)
        .where(
            DungeonRun.hero_name == current_hero.hero_name,
            DungeonRun.wing_id == wing_id,
            DungeonRun.status == "in_progress",
        )
        .order_by(desc(DungeonRun.updated_at))
    )
    result = await db.execute(stmt)
    run_record = result.scalar_one_or_none()

    if not run_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No active run found for wing '{wing_id}'",
        )
    return run_record


@router.post("/runs/{wing_id}/abandon")
async def abandon_dungeon_run(
    wing_id: str,
    current_hero: User = Depends(get_current_hero),
    db: AsyncSession = Depends(get_db),
):
    """Abandon or clear an active run for a wing to allow starting fresh."""
    stmt = (
        select(DungeonRun)
        .where(
            DungeonRun.hero_name == current_hero.hero_name,
            DungeonRun.wing_id == wing_id,
            DungeonRun.status == "in_progress",
        )
    )
    result = await db.execute(stmt)
    runs = result.scalars().all()

    for r in runs:
        r.status = "abandoned"

    await db.commit()
    return {"message": f"Active dungeon run for {wing_id} abandoned successfully", "abandoned_count": len(runs)}
