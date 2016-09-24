from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True)
    chapters = relationship("Chapter", back_populates="series")

    def __repr__(self):
        return "<Series %r>" % self.title


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True)
    body = Column(String(1000000))
    series_id = Column(Integer, ForeignKey("series.id"))
    series = relationship("Series", back_populates="chapters")

    def __repr__(self):
        return "<Chapter %r>" % (self.series.title + ": " + self.title)
