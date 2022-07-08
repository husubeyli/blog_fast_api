from token import OP
from typing import Dict, List, Optional
from fastapi import Body
from pydantic import BaseModel


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
