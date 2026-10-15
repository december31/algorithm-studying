from typing import List, Optional
from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import generate_hero_token, hash_incantation, verify_incantation
from app.models.user import User
from app.schemas.auth import (
    HeroLogin,
    HeroProfile,
    HeroSignUp,
    MarkProblemPassed,
    PassedProblemsResponse,
)

router = APIRouter()


async def get_current_hero(
    authorization: Optional[str] = Header(None),
    x_hero_token: Optional[str] = Header(None),
    db: AsyncSession = Depends(get_db),
) -> User:
    """Dependency to extract and validate the authenticated hero from headers."""
    token: Optional[str] = None
    if authorization:
        parts = authorization.split()
        if len(parts) == 2 and parts[0].lower() == "bearer":
            token = parts[1]
        else:
            token = authorization
    elif x_hero_token:
        token = x_hero_token

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No magical credentials provided. Please sign in or invoke your hero name.",
        )

    stmt = select(User).where(User.auth_token == token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The dungeon spirits do not recognize this token. Please log in again.",
        )

    return user


@router.post("/signup", response_model=HeroProfile, status_code=status.HTTP_201_CREATED)
async def signup(
    payload: HeroSignUp,
    db: AsyncSession = Depends(get_db),
):
    """Register a new adventurer using a hero name and secret incantation (no verification needed)."""
    clean_name = payload.hero_name.strip()
    if not clean_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Every adventurer needs a true name!",
        )

    # Check if hero name is already claimed
    stmt = select(User).where(User.hero_name.ilike(clean_name))
    result = await db.execute(stmt)
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An adventurer named '{clean_name}' already walks the dungeon halls! Choose another title or sign in.",
        )

    token = generate_hero_token()
    user = User(
        hero_name=clean_name,
        incantation_hash=hash_incantation(payload.secret_incantation),
        auth_token=token,
        passed_problems=[],
        level=1,
        xp=0,
        dungeon_floor=1,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return HeroProfile(
        id=user.id,
        hero_name=user.hero_name,
        level=user.level,
        xp=user.xp,
        dungeon_floor=user.dungeon_floor,
        passed_problems=user.passed_problems or [],
        token=token,
        created_at=user.created_at,
    )


@router.post("/login", response_model=HeroProfile)
async def login(
    payload: HeroLogin,
    db: AsyncSession = Depends(get_db),
):
    """Authenticate with your hero name and secret incantation."""
    clean_name = payload.hero_name.strip()
    stmt = select(User).where(User.hero_name.ilike(clean_name))
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user or not verify_incantation(payload.secret_incantation, user.incantation_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The dungeon doors remain barred. Invalid adventurer name or secret incantation.",
        )

    # Issue or refresh session token
    if not user.auth_token:
        user.auth_token = generate_hero_token()
        await db.commit()
        await db.refresh(user)

    return HeroProfile(
        id=user.id,
        hero_name=user.hero_name,
        level=user.level,
        xp=user.xp,
        dungeon_floor=user.dungeon_floor,
        passed_problems=user.passed_problems or [],
        token=user.auth_token,
        created_at=user.created_at,
    )


@router.get("/me", response_model=HeroProfile)
async def get_my_profile(
    current_hero: User = Depends(get_current_hero),
):
    """Retrieve the logged in adventurer's profile and stats."""
    return HeroProfile(
        id=current_hero.id,
        hero_name=current_hero.hero_name,
        level=current_hero.level,
        xp=current_hero.xp,
        dungeon_floor=current_hero.dungeon_floor,
        passed_problems=current_hero.passed_problems or [],
        token=current_hero.auth_token,
        created_at=current_hero.created_at,
    )


@router.get("/passed-problems", response_model=PassedProblemsResponse)
async def get_passed_problems(
    current_hero: User = Depends(get_current_hero),
):
    """List all problems passed / conquered by the current hero."""
    passed = current_hero.passed_problems or []
    return PassedProblemsResponse(
        hero_name=current_hero.hero_name,
        passed_problems=passed,
        total_passed=len(passed),
    )


@router.post("/passed-problems", response_model=PassedProblemsResponse)
async def mark_problem_passed(
    payload: MarkProblemPassed,
    current_hero: User = Depends(get_current_hero),
    db: AsyncSession = Depends(get_db),
):
    """Mark a problem as passed so the dungeon avoids showing it again."""
    passed = list(current_hero.passed_problems or [])
    clean_id = payload.problem_id.strip()

    if clean_id and clean_id not in passed:
        passed.append(clean_id)
        current_hero.passed_problems = passed
        current_hero.xp += 100
        # Level up every 300 XP
        current_hero.level = 1 + (current_hero.xp // 300)
        await db.commit()
        await db.refresh(current_hero)

    return PassedProblemsResponse(
        hero_name=current_hero.hero_name,
        passed_problems=current_hero.passed_problems or [],
        total_passed=len(current_hero.passed_problems or []),
    )


@router.delete("/passed-problems/{problem_id}", response_model=PassedProblemsResponse)
async def unmark_problem_passed(
    problem_id: str,
    current_hero: User = Depends(get_current_hero),
    db: AsyncSession = Depends(get_db),
):
    """Remove a problem from passed list (e.g. to allow replaying)."""
    passed = list(current_hero.passed_problems or [])
    clean_id = problem_id.strip()

    if clean_id in passed:
        passed.remove(clean_id)
        current_hero.passed_problems = passed
        await db.commit()
        await db.refresh(current_hero)

    return PassedProblemsResponse(
        hero_name=current_hero.hero_name,
        passed_problems=current_hero.passed_problems or [],
        total_passed=len(current_hero.passed_problems or []),
    )
