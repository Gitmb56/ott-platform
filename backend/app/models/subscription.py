from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan = Column(String)  # basic, premium, vip
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_active = Column(Integer, default=1)

    # Relationships
    user = relationship("User")