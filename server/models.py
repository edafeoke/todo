'''A module containing all models'''

import routes
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Todo(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='todos')
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    
    todos = relationship('Todo', back_populates='user')
    