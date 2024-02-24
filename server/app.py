'''Application entry point'''

from fastapi import FastAPI
import uvicorn
import models
from database import engine
from routes import user, todo, auth


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(todo.router)
app.include_router(user.router)
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run(app='app:app', host='localhost', port=3000, reload=True)
