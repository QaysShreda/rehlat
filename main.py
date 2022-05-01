from fastapi import FastAPI

from db.database import engine
from router import governorate, entity,image
from db.models import models
from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.include_router(governorate.router)
app.include_router(entity.router)
app.include_router(image.router)


@app.get("/")
def root():
    return "Hello World"


app.mount('/images',StaticFiles(directory="images"),name='images')

models.Base.metadata.create_all(engine)


