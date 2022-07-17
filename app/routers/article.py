from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import ArticleBase, ArticleDisplay
from schemas import UserDisplay
from typing import List

from db.databse import get_db
from db import db_article


router = APIRouter(
    prefix="/articles",
    tags=["articles"],
)


@router.post('/', response_model=ArticleDisplay)
async def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


@router.get('/all', response_model=List[ArticleDisplay])
async def get_all_articles(db: Session = Depends(get_db)):
    return db_article.getl_all_article(db)


@router.get('/{article_id}', response_model=ArticleDisplay)
async def get_article(article_id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, article_id)