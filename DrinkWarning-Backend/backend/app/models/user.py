from sqlalchemy import Column, Integer, String, Float, DateTime
from app.core.database import Base
import datetime


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    age = Column(Integer)
    gender = Column(String)
    baseline_heart_rate = Column(Float, default=70)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)