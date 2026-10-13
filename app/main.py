"""
FastAPI CRUD Operation Practice Example
-------------------------------------------------------------------
This file demonstrates how to create, read, update, and delete posts
using an in-memory list while establishing a PostgreSQL connection.
-------------------------------------------------------------------
"""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import auth, post, user ,vote
from .config import settings


# models.Base.metadata.create_all(bind=engine, checkfirst=True)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://www.google.com",
    ],           # Allow requests from these specific origins
    allow_credentials=True,          # Allow cookies / authentication headers
    allow_methods=["*"],             # Allow all standard HTTP methods (GET, POST, etc.)
    allow_headers=["*"],             # Allow all custom or standard HTTP headers
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


 
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI CRUD Practice Session"}


