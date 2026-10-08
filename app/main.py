"""
FastAPI CRUD Operation Practice Example
-------------------------------------------------------------------
This file demonstrates how to create, read, update, and delete posts
using an in-memory list while establishing a PostgreSQL connection.
-------------------------------------------------------------------
"""


from fastapi import FastAPI
from . import models
from .database import engine
from .routers import auth, post, user

models.Base.metadata.create_all(bind=engine, checkfirst=True)
app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI CRUD Practice Session"}


