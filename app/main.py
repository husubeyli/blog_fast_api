from sys import prefix
from fastapi import FastAPI, HTTPException
from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse, PlainTextResponse

# from fastapi_admin.app import app as admin_app
# from fastapi_admin.providers.login import UsernamePasswordProvider
# from examples.models import Admin
# import aioredis

from exceptions import StroyException
from routers import article
from routers import blog_get
from routers import blog_post
from routers import user
from routers import product

from db import models
from db.databse import engine

app = FastAPI()
# app.mount("/admin", admin_app)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)


@app.get("/", tags=['home'])
def index():
    return RedirectResponse(url='/docs/')


@app.exception_handler(StroyException)
def story_exception_handler(request: Request, exc: StroyException):
    return JSONResponse(
        status_code=418,
        content={
            'detail': exc.name
        }
    )
    
# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StroyException):
#     return PlainTextResponse(str(exc), status_code=400)


models.Base.metadata.create_all(engine)
