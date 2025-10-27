from pydantic import BaseModel, EmailStr, Field
from pydantic import ConfigDict
from typing import Optional, Annotated
from datetime import datetime, timezone


class UserBase(BaseModel):
    email: EmailStr
    username: Annotated[str, Field(min_length=3, max_length=50)]

    created_at: datetime = Field(
            default_factory=lambda: datetime.now(timezone.utc)
        )

    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    password: str
    confirm_password: str


class UserResponse(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[Annotated[str, Field(min_length=3, max_length=50)]] = None

    model_config = ConfigDict(from_attributes=True)
