from fastapi import APIRouter,Depends,status,Response
from fastapi.exceptions import  HTTPException
from typing import List

from db import db_gov
from db.database import get_db
from schemas.schema import GovernorateBase,GovernorateDisplay
from sqlalchemy.orm import  Session

router = APIRouter(
    prefix='/governorate',
    tags=['Governorates']
)

@router.post('')
def create(request:GovernorateBase,db:Session=Depends(get_db)):
    return db_gov.create(db,request)

@router.get('/{id}')
def get_governorate(db:Session=Depends(get_db),id=id):
    response = Response()
    return db_gov.get_governorate(db,id)

@router.get('/all',response_model=List[GovernorateDisplay],description="Get All Governorate")
def get_all_governorates(db:Session=Depends(get_db)):
    return db_gov.get_all(db)



@router.put('/update/{id}')
def update_gov(request:GovernorateBase,db:Session=Depends(get_db),id=id):
    return db_gov.update_gov(request,db,id)


@router.delete('/delete/{id}')
def delete(id:int,db:Session= Depends(get_db)):
    return db_gov.delete(db,id)
