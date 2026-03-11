from fastapi import APIRouter

from app.dto import UserCreate, UserRead, UserUpdate
from app.users import auth_backend, fastapi_users


router = APIRouter(prefix="/api", tags=["auth"])


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
)

