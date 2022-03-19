from sqlalchemy.orm import Session

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
