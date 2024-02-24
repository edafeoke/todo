'''user route module
'''
import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db, Session
import schemas
import models
from typing import List
# from sqlalchemy.orm import Session
from controllers.user import update, delete, all, read, create

router = APIRouter (
    prefix='/user',
    tags=['users'],
    dependencies=[],
    responses={404: {'description': 'not found'}})


@router.get(
    '/',
    response_model=List[schemas.ShowUser],
    status_code=status.HTTP_200_OK,
    )
def all_users(db: Session=Depends(get_db)):
    return all(db)

@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def get_user(id, db: Session=Depends(get_db)):
    return read(id, db)

@router.put('/{id}')
def update_user(id: int, request: schemas.User, db: Session=Depends(get_db)):
    return update(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_user(id: int, db: Session=Depends(get_db)):
    return delete(id, db)

    
@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session=Depends(get_db)):
    
    return create(request, db)