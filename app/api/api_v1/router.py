from fastapi import APIRouter
from app.api.api_v1.handlers.user import user_router
from app.api.auth.jwt import auth_router
from app.api.api_v1.handlers.task import task_router

router = APIRouter()

router.include_router(
    user_router, prefix="/users", tags=["users"]
)

router.include_router(
    auth_router, prefix="/auth", tags=["auth"]
)

router.include_router(
    task_router, prefix="/tasks", tags=["tasks"]
)
