from fastapi import FastAPI

from db.database import engine
from router import governorate, entity
from db.models import models

app = FastAPI()

app.include_router(governorate.router)
app.include_router(entity.router)


@app.get("/")
def root():
    return "Hello World"

models.Base.metadata.create_all(engine)
