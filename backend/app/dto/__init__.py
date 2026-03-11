from typing import Optional
from uuid import UUID

from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class CarBase(BaseModel):
    make: str
    model: str
    year: int
    price: int
    color: Optional[str] | None = None
    url: str


class CarRead(CarBase):
    id: int

    class Config:
        from_attributes = True

