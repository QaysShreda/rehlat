from db.models.models import DbGovernorate
from schemas.schema import GovernorateBase
from sqlalchemy.orm import Session


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