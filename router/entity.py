from fastapi import APIRouter

from db import db_entity
from db.database import get_db
from schemas.schema import EntityBase
from sqlalchemy.orm import Session
from fastapi import Depends


router = APIRouter(
    prefix="/entity",
    tags=['Entity']
)

@router.post('/')
def create_entity(reqest:EntityBase,db:Session =Depends(get_db)):
    return db_entity.create_entity(db,reqest)