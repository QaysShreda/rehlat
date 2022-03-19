from datetime import datetime
from typing import List,Tuple,Text
from pydantic import BaseModel

class GovernorateBase(BaseModel):
    name :str
    description:str
    lat: float
    long: float
    image :str

class GovernorateDisplay(BaseModel):
    name :str
    description:str
    lat: float
    long: float
    image :str
    class Config():
        orm_mode = True

class EntityBase(BaseModel):
    name :str
    lat: float
    long : float
    type :str
    description :str
    tel :str
    mobile :str
    page :str
    face :str
    cover_image :str
    image :str
    work_hour :str
    rate : int
    recommend :int
    entertainment :bool
    restorant :bool
    archeological :bool
    sites :bool
    hotels :bool
    Shopping :bool
    Resort :bool
    water :bool
    sport :bool
    track :bool
    governorate_id :int