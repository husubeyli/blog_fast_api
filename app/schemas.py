from typing import List, Optional
from pydantic import BaseModel


# Articel inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config():
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    articles: List[Article] = []

    class Config():
        orm_mode = True


# User inside Article
class User(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creater_id: int


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config():
        orm_mode = True
