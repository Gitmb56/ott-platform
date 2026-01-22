from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_active_user
from app.models.user import User

router = APIRouter()


@router.get("/stream/{video_id}")
def stream_video(
    video_id: int,
    current_user: User = Depends(get_current_active_user),
):
    """
    Stream video content.
    """
    # TODO: Implement video streaming logic
    return {"message": f"Streaming video {video_id}"}