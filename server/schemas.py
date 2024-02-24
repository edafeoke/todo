'''A modules containing all pydantic schemas of all models'''


from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Todo(BaseModel):
    # id: int
    title: str = ''
    description: str = ''
    is_completed: bool = False
    user_id: int
    
    class Config():
        orm_mode = True

        
class UpdateTodo(BaseModel):
    title: Optional[str]
    description: Optional[str]
    is_completed: Optional[bool]
    
    class Config():
        orm_mode = True

class User(BaseModel):
    email: str
    password: str
    name: str
    
    class Config():
        orm_mode = True

class ShowTodo(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool

    class Config():
        orm_mode = True
        
class ShowUser(BaseModel):
    email: str
    name: str
    created_at: datetime
    updated_at: datetime
    todos: List[ShowTodo]
    
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str