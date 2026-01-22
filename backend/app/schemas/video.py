from typing import Optional

from pydantic import BaseModel


class VideoBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    file_path: Optional[str] = None
    thumbnail_path: Optional[str] = None
    duration: Optional[int] = None


class VideoCreate(VideoBase):
    title: str
    description: str
    file_path: str


class VideoUpdate(VideoBase):
    pass


class Video(VideoBase):
    id: int
    title: str
    description: str
    owner_id: int

    class Config:
        orm_mode = True