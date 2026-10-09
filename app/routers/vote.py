from fastapi import FastAPI, APIRouter, Depends, HTTPException, Response, status
from .. import schemas, database , models , oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix = "/vote",
    tags = ['Vote']

)

@router.post("/", status_code = status.HTTTP_201_CREATED)
def vote(vote: schemas.Vote,db: Session = Depends(database.get_db),current_user:int = Depends
         (oauth2.get_current_user)):

    if (vote.dir == 1):
        db.query(models.Vote).filter(models.Vote.post_id == vote.post_id)
    else:
        