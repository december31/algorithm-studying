from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from sqlalchemy import DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Problem(Base):
    __tablename__ = "problems"

    id: Mapped[str] = mapped_column(String(100), primary_key=True, index=True)
    wing_id: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    floor: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    difficulty: Mapped[str] = mapped_column(String(20), index=True, nullable=False)  # easy, medium, hard
    visualizer_type: Mapped[str] = mapped_column(String(50), default="array", nullable=False)
    monster: Mapped[Dict[str, Any]] = mapped_column(JSON, default=dict, nullable=False)
    description: Mapped[str] = mapped_column(Text, default="", nullable=False)
    examples: Mapped[List[Dict[str, Any]]] = mapped_column(JSON, default=list, nullable=False)
    constraints: Mapped[List[str]] = mapped_column(JSON, default=list, nullable=False)
    starter_code: Mapped[str] = mapped_column(Text, default="", nullable=False)
    solution_code: Mapped[str] = mapped_column(Text, default="", nullable=False)
    function_name: Mapped[str] = mapped_column(String(100), nullable=False)
    test_cases: Mapped[List[Dict[str, Any]]] = mapped_column(JSON, default=list, nullable=False)
    hints: Mapped[List[str]] = mapped_column(JSON, default=list, nullable=False)
    python: Mapped[Dict[str, Any]] = mapped_column(JSON, default=dict, nullable=False)
    leetcode_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    leetcode_title: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    leetcode_url: Mapped[Optional[str]] = mapped_column(String(300), nullable=True)
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
