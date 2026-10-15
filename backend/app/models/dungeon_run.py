from datetime import datetime, timezone
from sqlalchemy import DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class DungeonRun(Base):
    __tablename__ = "dungeon_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    hero_name: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    wing_id: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    current_floor: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    max_floor_reached: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="in_progress", nullable=False)  # in_progress, completed, abandoned
    run_catalog: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    current_problem_id: Mapped[str] = mapped_column(String(100), nullable=False)
    code: Mapped[str] = mapped_column(Text, default="", nullable=False)
    language: Mapped[str] = mapped_column(String(20), default="python", nullable=False)
    hp: Mapped[int] = mapped_column(Integer, default=100, nullable=False)
    max_hp: Mapped[int] = mapped_column(Integer, default=100, nullable=False)
    gold: Mapped[int] = mapped_column(Integer, default=50, nullable=False)
    potions: Mapped[int] = mapped_column(Integer, default=2, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
