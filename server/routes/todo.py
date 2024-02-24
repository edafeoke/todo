'''todo route module
'''
import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
import schemas
import models
from typing import List
from sqlalchemy.orm import Session
from controllers.todo import all, create, delete, read, update

router = APIRouter (
    prefix='/todos',
    tags=['todos'],
    dependencies=[],
    responses={404: {'description': 'not found'}})

@router.get('/', response_model=List[schemas.ShowTodo], status_code=status.HTTP_200_OK)
def all_todo(db: Session=Depends(get_db)):
    return all(db)

@router.get('/{id}', response_model=schemas.ShowTodo, status_code=status.HTTP_200_OK)
def get_todos(id, db: Session=Depends(get_db)):
    return read(id, db)

@router.put('/{id}')
def update_todo(id: int, request: schemas.Todo, db: Session=Depends(get_db)):
    return update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_todo(id: int, db: Session=Depends(get_db)):
    return delete(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_todo(request: schemas.Todo, db: Session=Depends(get_db)):
    return create(request, db)