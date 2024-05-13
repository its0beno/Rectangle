from sqlalchemy import Column, Float, Integer
from database import Base


class Rectangle(Base):
    __tablename__ = "rectangles"
    id = Column(Integer, primary_key=True)
    x1 = Column(Float, nullable=False)
    y1 = Column(Float, nullable=False)
    x2 = Column(Float, nullable=False)
    y2 = Column(Float, nullable=False)
