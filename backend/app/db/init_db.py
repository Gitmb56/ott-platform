from sqlalchemy.orm import Session

from app.db.session import SessionLocal


def init_db(db: Session) -> None:
    # Import all models here to ensure they are registered with SQLAlchemy
    from app.models import user, video, episode, subscription  # noqa: F401

    # Create tables
    from app.db.base import Base
    Base.metadata.create_all(bind=db.bind)