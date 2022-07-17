from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm.session import Session
from fastapi.encoders import jsonable_encoder

from db.models import ArticleDb
from schemas import ArticleBase
from exceptions import StroyException

def create_article(db: Session, request: ArticleBase):
    if request.content.startswith('Once upon a time'):
        raise StroyException('No stories please')
    new_article = ArticleDb(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creater_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, article_id: int):
    article = db.query(ArticleDb).filter(ArticleDb.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Article with id {article_id} not found')


def getl_all_article(db: Session):
    return db.query(ArticleDb).all()
