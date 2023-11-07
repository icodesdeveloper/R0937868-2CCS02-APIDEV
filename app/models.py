from sqlalchemy import create_engine, Column, Integer, String

from database import Base
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(25), index=True)
    author = Column(String(25), index=True)
    genre = Column(String(25), index=True)