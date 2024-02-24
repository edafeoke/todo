'''user route module
'''
import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Depends
from database import get_db
import schemas
import models
from typing import List
from sqlalchemy.orm import Session

router = APIRouter (
    prefix='/auth',
    tags=['auth'],
    dependencies=[],
    responses={404: {'description': 'not found'}})


@router.post('/login')
def login(request: schemas.Login, db: Session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No user with the specified email address!')
    else:
        return user