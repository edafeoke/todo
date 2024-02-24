'''todo controller module: holding all todo route functions
'''
import datetime
import models

def all(db):
    todos = db.query(models.Todo).all()
    return todos

def read(id, db):
    todo = db.query(models.Todo).filter_by(id = id).first()
    return todo

def update(id, request, db):
    update_data = request.model_dump()
    
    # Filter out None values, if any
    update_data = {k: v for k, v in update_data.items() if v is not ''}
    update_data['updated_at'] = datetime.datetime.now()

    db.query(models.Todo).filter(models.Todo.id == id).update(update_data)
    
    # Commit the changes to the database
    db.commit()
    
    # Return a success message
    return {'message': 'Updated Successfully'}

def delete(id, db):
    db.query(models.Todo).filter_by(id = id).delete()
    db.commit()
    return {"message": "Successfully deleted the todo with id {id}"}

def create(request, db):
    '''Create a new todo'''
    
    new_todo = models.Todo(
        title=request.title,
        description=request.description,
        is_completed=False,
        user_id=request.user_id
        )
    todos = db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo