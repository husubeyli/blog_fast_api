from typing import Optional
from fastapi import Body
from pydantic import BaseModel



class BlogModel(BaseModel):
    title: str
    content: str = Body('Hello World!')
    count_comment: int
    published: Optional[bool]
    
