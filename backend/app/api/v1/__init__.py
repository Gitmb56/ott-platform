# API v1 module
from fastapi import APIRouter

from .routes import auth, users, videos, subscriptions, streaming

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(videos.router, prefix="/videos", tags=["videos"])
api_router.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])
api_router.include_router(streaming.router, prefix="/streaming", tags=["streaming"])
