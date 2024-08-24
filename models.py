# # models.py

# from sqlalchemy import Column, Integer, String, Date
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Article(Base):
#     __tablename__ = "articles"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     abstract = Column(String, nullable=True)
#     url = Column(String, nullable=False)
#     published_date = Column(Date, nullable=True)
#     sentiment = Column(String, nullable=True)
#     topic = Column(String, nullable=True)

from sqlalchemy import Column, Integer, String, Text
from database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    abstract = Column(Text)
    url = Column(String)
    published_date = Column(String)
    sentiment = Column(String, default='Not analyzed')
    topic = Column(String, default='Not categorized')
