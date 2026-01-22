from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_active_user
from app.models.user import User

router = APIRouter()


@router.get("/")
def get_subscription(
    current_user: User = Depends(get_current_active_user),
):
    """
    Get user subscription.
    """
    # TODO: Implement subscription logic
    return {"subscription": "premium"}