from sqlalchemy import func, Column, Integer, String, Float, DateTime

from ..database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    director = Column(String, index=True)
    release_year = Column(Integer, index=True)
    genre = Column(String, index=True)
    rating = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
