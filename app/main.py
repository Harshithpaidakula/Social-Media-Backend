"""
FastAPI CRUD Operation Practice Example
-------------------------------------------------------------------
This file demonstrates how to create, read, update, and delete posts
using an in-memory list while establishing a PostgreSQL connection.
-------------------------------------------------------------------
"""

import time
from typing import Optional,List

import psycopg2  # type: ignore[import-not-found]
from fastapi import FastAPI, HTTPException, Response, status, Depends
from psycopg2.extras import RealDictCursor  # type: ignore[import-not-found]
from sqlalchemy.orm import Session  # type: ignore

from . import models, schemas , utils
from .database import SQLALCHEMY_DATABASE_URL, engine, get_db
from .routers import auth, post, user

models.Base.metadata.create_all(bind=engine, checkfirst=True)

 
while True:
    try:
        conn = psycopg2.connect(SQLALCHEMY_DATABASE_URL)
        conn.autocommit = True
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)


app = FastAPI()






my_posts = [
    {"title": "Practice Session 1", "content": "Content block 1", "id": 1},
    {"title": "Practice Session 2", "content": "Content block 2", "id": 2},
]


def find_post(post_id: int):
    """Finds and returns a specific post by its ID."""
    for post in my_posts:
        if post.get("id") == post_id:
            return post
    return None


def find_index_post(post_id: int):
    """Finds and returns the index position of a post by its ID."""
    for index, post in enumerate(my_posts):
        if post.get("id") == post_id:
            return index
    return None 

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI CRUD Practice Session"}


