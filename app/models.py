from sqlalchemy import Column, Integer, String, Text, DateTime
from app.database import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    abstract = Column(Text)
    url = Column(String)
    published_date = Column(DateTime)
    sentiment = Column(String)
    topic = Column(String)
