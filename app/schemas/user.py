from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional, Annotated
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr = Field(...)
    username: Annotated[str, Field(min_length=3, max_length=50)] = Field(...)

    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    password: Annotated[str, Field(min_length=8, max_length=128)] = Field(...)


class UserResponse(UserBase):
    id: int = Field(...)
    is_active: bool = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = Field(None)
    username: Optional[Annotated[str, Field(min_length=3, max_length=50)]] = Field(None)
    is_active: Optional[bool] = Field(None)

    model_config = ConfigDict(from_attributes=True)


class UserPasswordUpdate(BaseModel):
    current_password: str = Field(...)
    new_password: Annotated[str, Field(min_length=8, max_length=128)] = Field(...)


class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
