import asyncio
import json
import logging
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func, select

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.database import AsyncSessionLocal, init_db
from app.models.problem import Problem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def restore_problems_if_needed():
    """Self-healing restoration: if problems table is empty, auto-seed from master JSON backup."""
    try:
        async with AsyncSessionLocal() as session:
            res = await session.execute(select(func.count()).select_from(Problem))
            problem_count = res.scalar() or 0
            logger.info(f"Database currently contains {problem_count} problems.")

            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            candidate_paths = [
                os.path.join(base_dir, "data", "problems_backup.json"),
                "/app/data/problems_backup.json",
                os.path.join(os.path.dirname(base_dir), "public", "problems", "catalog.json"),
            ]
            backup_file = next((p for p in candidate_paths if os.path.exists(p)), None)

            if problem_count == 0 and backup_file:
                logger.info(f"Problems table is empty! Restoring from master backup: {backup_file}...")
                with open(backup_file, "r", encoding="utf-8") as f:
                    backup_data = json.load(f)

                restored = 0
                for item in backup_data:
                    prob = Problem(
                        id=item["id"],
                        wing_id=item["wingId"],
                        floor=item.get("floor", 1),
                        title=item["title"],
                        difficulty=item["difficulty"],
                        visualizer_type=item.get("visualizerType", "array"),
                        monster=item.get("monster", {}),
                        description=item.get("description", ""),
                        examples=item.get("examples", []),
                        constraints=item.get("constraints", []),
                        starter_code=item.get("starterCode", ""),
                        solution_code=item.get("solutionCode", ""),
                        function_name=item.get("functionName", "solution"),
                        test_cases=item.get("testCases", []),
                        hints=item.get("hints", []),
                        python=item.get("python", {}),
                        leetcode_id=item.get("leetcodeId"),
                        leetcode_title=item.get("leetcodeTitle"),
                        leetcode_url=item.get("leetcodeUrl"),
                    )
                    session.add(prob)
                    restored += 1
                await session.commit()
                logger.info(f"Self-healing complete: Restored {restored} problems into PostgreSQL database.")
    except Exception as e:
        logger.error(f"Error during database problem self-healing: {e}", exc_info=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan: initialize database tables with retry and self-healing data seed."""
    logger.info("Starting up Algo-Dungeon backend...")
    max_retries = 10
    retry_interval = 2

    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Connecting to database (attempt {attempt}/{max_retries})...")
            await init_db()
            logger.info("Database initialized successfully.")
            await restore_problems_if_needed()
            break
        except Exception as e:
            logger.warning(f"Database not ready yet ({e}). Retrying in {retry_interval}s...")
            if attempt == max_retries:
                logger.error("Could not connect to database after maximum retries. Continuing startup.")
            else:
                await asyncio.sleep(retry_interval)

    yield

    logger.info("Shutting down Algo-Dungeon backend...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Configure CORS
origins = settings.CORS_ORIGINS if isinstance(settings.CORS_ORIGINS, list) else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to Algo-Dungeon API",
        "docs": "/docs",
        "health": f"{settings.API_V1_STR}/health",
        "version": settings.VERSION,
    }


# Include API v1 router
app.include_router(api_router, prefix=settings.API_V1_STR)
