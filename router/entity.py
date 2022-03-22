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

@router.get('/')
def get_all_entities(db:Session =Depends(get_db)):
    return db_entity.get_all_entities(db)

@router.get('/{id}')
def get_entity(id:int,db:Session =Depends(get_db)):
    return db_entity.get_entity(db,id)

@router.put('/update/{id}')
def update_entity(id:int,request:EntityBase,db:Session=Depends(get_db)):
    return db_entity.update_entity(db,id,request)

@router.delete('delete/{id}')
def delete_entity(id:int,db:Session=Depends(get_db)):
    return db_entity.delete_entity(db,id)