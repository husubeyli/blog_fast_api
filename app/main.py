from fastapi import FastAPI
from routers import blog_get, blog_post
from sqlalchemy.engine.base import Engine
from db import models


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/")
def index():
    return {"data": {"name": 'husubayli'}}

models.Base.metadata.create_all(Engine)