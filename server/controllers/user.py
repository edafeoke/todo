from security.hash import Hashing
from datetime import datetime
import models

hash_password = Hashing().hash_password

def create(request, db):
    
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=Hashing.hash_password(password=request.password),
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update(id, request, db):
    # Extract the fields that are present in the request
    update_data = request.model_dump()
    
    # Filter out None values, if any
    update_data = {k: v for k, v in update_data.items() if v is not ''}
    update_data['updated_at'] = datetime.now()
    if update_data['password'] != '':
        update_data['password'] = hash_password(update_data['password'])
        
    # Update the fields with the provided data
    db.query(models.User).filter(models.User.id == id).update(update_data)
    
    # Commit the changes to the database
    db.commit()
    
    # Return a success message
    return {'message': 'User data modified Successfully'}

def delete(id: int,db):
    db.query(models.User).filter_by(id = id).delete(synchronize_session=False)
    db.commit()
    return {"message": "Successfully deleted the user with id {id}"}

def all(db):
    users = db.query(models.User).all()
    return users

def read(id, db):
    user = db.query(models.User).filter_by(id = id).first()
    return user