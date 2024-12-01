from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.services.user_service import UserService
from app.core.security import create_access_token, create_refresh_token
from app.schemas.auth_schema import TokenSchema
from app.schemas.user_schema import UserDetail
from app.models.user_model import User
from app.api.dependencies.user_deps import get_current_user

auth_router = APIRouter()

@auth_router.post("/login", summary="Cria o access token e o refresh token", response_model=TokenSchema)
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        email = data.username,
        password = data.password
    )
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail ou senha estão invalidos!"
        )
    
    return {
        "access_token": create_access_token(usuario.user_id),
        "refresh_token": create_refresh_token(usuario.user_id)
    }


@auth_router.post("/teste-token", summary="Testando o token", response_model=UserDetail)
async def teste_token(user: User = Depends(get_current_user)):
    return user
