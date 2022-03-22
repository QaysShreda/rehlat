from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from db.models.models import DbEntity
from schemas.schema import EntityBase


def create_entity(db:Session,request:EntityBase):
    new_entity = DbEntity(
    name = request.name,
    lat = request.lat,
    long = request.long,
    type = request.type,
    description = request.description,
    tel = request.tel,
    mobile = request.mobile,
    page = request.page,
    face = request.face,
    cover_image = request.cover_image,
    image = request.image,
    work_hour = request.work_hour,
    rate = request.rate,
    recommend = request.recommend,
    entertainment = request.entertainment,
    restorant = request.restorant,
    archeological = request.archeological,
    sites = request.sites,
    hotels = request.hotels,
    Shopping = request.Shopping,
    Resort = request.Resort,
    water = request.water,
    sport = request.sport,
    track = request.track,
    governorate_id = request.governorate_id
    )
    db.add(new_entity)
    db.commit()
    db.refresh(new_entity)
    return new_entity

def get_all_entities(db:Session):
    return db.query(DbEntity).all()

def get_entity(db:Session,id:int):
    entity = db.query(DbEntity).filter(DbEntity.id == id).first()
    if not entity:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Entity not fount")
    return entity

def update_entity(db:Session,id:int,request:EntityBase):
    entity = db.query(DbEntity).filter(DbEntity.id == id).first()
    if not entity:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Entity not fount")
    entity.update({
    DbEntity.name : request.name,
    DbEntity.lat : request.lat,
    DbEntity.long : request.long,
    DbEntity.type : request.type,
    DbEntity.description : request.description,
    DbEntity.tel : request.tel,
    DbEntity.mobile : request.mobile,
    DbEntity.page : request.page,
    DbEntity.face : request.face,
    DbEntity.cover_image : request.cover_image,
    DbEntity.image : request.image,
    DbEntity.work_hour : request.work_hour,
    DbEntity.rate : request.rate,
    DbEntity.recommend : request.recommend,
    DbEntity.entertainment : request.entertainment,
    DbEntity.restorant : request.restorant,
    DbEntity.archeological : request.archeological,
    DbEntity.sites : request.sites,
    DbEntity.hotels : request.hotels,
    DbEntity.Shopping : request.Shopping,
    DbEntity.Resort : request.Resort,
    DbEntity.water : request.water,
    DbEntity.sport : request.sport,
    DbEntity.track : request.track,
    DbEntity.governorate_id : request.governorate_id
    })
    db.commit()
    return "Update Successfully"


def delete_entity(db:Session,id):
    entity = db.query(DbEntity).filter(DbEntity.id == id)
    if not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Entity not found")
    db.deleted(entity)
    db.commit()
    return "Delete Successfully"
