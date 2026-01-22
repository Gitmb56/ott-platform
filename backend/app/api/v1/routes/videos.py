from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user
from app.db.session import get_db
from app.models.user import User
from app.models.video import Video
from app.schemas.video import Video as VideoSchema

router = APIRouter()


@router.get("/", response_model=List[VideoSchema])
def read_videos(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user),
):
    """
    Retrieve videos.
    """
    videos = db.query(Video).offset(skip).limit(limit).all()
    return videos


@router.get("/{video_id}", response_model=VideoSchema)
def read_video(
    video_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """
    Get video by ID.
    """
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video