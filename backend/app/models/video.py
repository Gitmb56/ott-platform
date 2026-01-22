from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    file_path = Column(String)
    thumbnail_path = Column(String)
    duration = Column(Integer)  # in seconds
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    owner = relationship("User", back_populates="videos")
    episodes = relationship("Episode", back_populates="video")