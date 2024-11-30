from fastapi import APIRouter

task_router = APIRouter()

@task_router.get("/teste")
async def teste():
    return "Tarefas listadas"

