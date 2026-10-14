from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# connection string 
# engine is responsible for connection
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL or (
    f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}"
    f"@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
)
SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# 2. The Yield Dependency Function
# to send sql statement when we got request and close
def get_db():
    db = SessionLocal()
    try:
        yield db  # This is injected into the endpoint
    finally:
        db.close()  # This runs AFTER the response is sent to the client
