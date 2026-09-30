# pyright: reportMissingImports=false
# This file is the ORM model file.
# In SQLAlchemy, each class here represents a database table.
# We use these classes to create/read/update/delete rows in the database.
# 'Base' is the base class from database.py. It gives us the SQLAlchemy model system.
# The dot before database means: import from the current package folder.

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base  

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key = True,nullable = True)
    title = Column(String,nullable = False)
    content = Column(String,nullable= False)
    published = Column(Boolean,server_default = 'True')
    #timestamp later
    content_at =Column(TIMESTAMP(timezone=True),nullable = False , server_default=text('now()'))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    content_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

