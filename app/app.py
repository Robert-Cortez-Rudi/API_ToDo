from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.user_model import User
from app.models.task_model import Task
from app.api.api_v1.router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title= settings.PROJECT_NAME,
    openapi_url= f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

 
@app.on_event("startup")
async def app_init():
    client_db = AsyncIOMotorClient(
        settings.MONGO_CONNECTION_STRING).todoapp
    

    await init_beanie(
        database = client_db,
        document_models = [
            User, Task
        ]
    )

app.include_router(
    router, prefix=settings.API_V1_STR
)
