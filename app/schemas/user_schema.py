from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

# Schema para input
class UserAuth (BaseModel):
    email: EmailStr = Field(..., description="E-mail do usuário")
    username: str = Field(
        ...,
        min_length=5,
        max_length=50,
        description="Username"
    )
    password: str = Field(
        min_length=5,
        max_length=20,
        description="Senha do usuário"
    )
    
# Schema para output
class UserDetail(BaseModel):
    user_id: UUID
    username: str
    email: str
