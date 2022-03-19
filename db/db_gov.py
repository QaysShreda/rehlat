from db.models.models import DbGovernorate
from schemas.schema import GovernorateBase,GovernorateDisplay
from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Response


def create(db:Session, request: GovernorateBase):
    new_gov = DbGovernorate(
         name = request.name,
         lat = request.lat,
         long = request.long,
         description = request.description,
         image = request.image

    )

    db.add(new_gov)
    db.commit()
    db.refresh(new_gov)
    return  new_gov

def get_all(db:Session):
    return db.query(DbGovernorate).all()

def get_governorate(db:Session,id:int):
    gov = db.query(DbGovernorate).filter(DbGovernorate.id == id).first()
    if not gov:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return gov

def update_gov(request:GovernorateBase,db:Session,id:int):
    gov = db.query(DbGovernorate).filter(DbGovernorate.id == id)
    if not gov:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    gov.update({
        DbGovernorate.name:request.name,
        DbGovernorate.lat:request.lat,
        DbGovernorate.long:request.long,
        DbGovernorate.description:request.description,
        DbGovernorate.image:request.image
    })
    db.commit()
    return "Done ..."


def delete(db:Session,id:int):
    gov = db.query(DbGovernorate).filter(DbGovernorate.id == id).first()
    if not gov:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f'Governorate with id : {id} not found')
    db.delete(gov)
    db.commit()
    return 'Done...'