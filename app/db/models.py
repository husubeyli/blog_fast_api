from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from typing import Dict, List, Optional
from fastapi import Body
from pydantic import BaseModel

from db.databse import Base



class UserDb(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    username = Column(String(50), unique=True, index=True)
    email = Column(String)
    password = Column(String)
    articles = relationship("ArticleDb", back_populates="user")
    
    
class ArticleDb(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    title = Column(String(50))
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserDb", back_populates="articles")


class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str = Body('Hello World!')
    count_comment: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key': 'val'}
    image: Optional[Image] = None