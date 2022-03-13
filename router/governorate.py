from fastapi import APIRouter,Depends,status
from fastapi.exceptions import  HTTPException
from typing import List

from db import db_gov
from db.database import get_db
from schemas.schema import GovernorateBase
from sqlalchemy.orm import  Session

router = APIRouter(
    prefix='/governorate',
    tags=['Gov']
)

@router.post('')
def create(request:GovernorateBase,db:Session=Depends(get_db)):
    return db_gov.create(db,request)