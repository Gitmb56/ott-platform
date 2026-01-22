from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Episode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    episode_number = Column(Integer)
    season_number = Column(Integer, default=1)
    file_path = Column(String)
    video_id = Column(Integer, ForeignKey("videos.id"))

    # Relationships
    video = relationship("Video", back_populates="episodes")