from fastapi import APIRouter, Body, Query
from models.blog import BlogModel

router = APIRouter(
    prefix = "/blogs",
    tags = ["blog"],
)



@router.post('/new')
def create_blog(blog: BlogModel, id: int = Body(default=1), version: int=1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }
    
@router.post('/new/{id}/comment')
def create_comment(
        blog: BlogModel, 
        id: int, 
        comment_id: int = Query(
            None,
            title = 'ID of the comment',
            description = 'Some description for comment_id',
            alias="comment_id",
            deprecated=True,
        )
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id
    }