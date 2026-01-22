# Schemas module for OTT Platform
from .auth import Token, TokenData, UserLogin, UserRegister
from .user import User, UserCreate, UserUpdate, UserInDB
from .video import Video, VideoCreate, VideoUpdate, VideoInDB

__all__ = [
    "Token", "TokenData", "UserLogin", "UserRegister",
    "User", "UserCreate", "UserUpdate", "UserInDB",
    "Video", "VideoCreate", "VideoUpdate", "VideoInDB"
]
