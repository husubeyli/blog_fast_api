from typing import List
from fastapi import APIRouter, Body, Query, Path
from models.blog import BlogModel

router = APIRouter(
    prefix="/blogs",
    tags=["blog"],
)


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(
        None,
        title='Title of the comment',
        description='Some description for comment_title',
        alias="comment_title",
        deprecated=True,
    ),
    content: str = Body(...,
                        min_length=10,
                        max_length=255,
                        regex=r'^[a-z\s]*$'
                        ),
    v: List[str] = Query(['1.0', '1.1', '1.2']),
    comment_id: int = Path(None, gt=5, le=10),
):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id
    }


def required_functionality():
    return {'message': 'This is a required functionality'}