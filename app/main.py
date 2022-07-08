from fastapi import FastAPI
from routers import blog_get
from routers import blog_post
from routers import user

from db import models
from db.databse import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)


@app.get("/")
def index():
    return {"data": {"name": 'husubayli'}}

models.Base.metadata.create_all(engine)