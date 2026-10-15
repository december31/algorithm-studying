from fastapi import APIRouter

from app.api.v1.endpoints import auth, dungeon, health, problems, progress, submissions

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(auth.router, prefix="/auth", tags=["Hero Authentication & Conquered Problems"])
api_router.include_router(dungeon.router, prefix="/dungeon", tags=["Dungeon Runs Progress"])
api_router.include_router(problems.router, prefix="/problems", tags=["Algorithm Challenges"])
api_router.include_router(submissions.router, prefix="/submissions", tags=["Submissions"])
api_router.include_router(progress.router, prefix="/progress", tags=["Progress"])
