from db.database import Base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,TupleType,Text,Boolean,Float
from sqlalchemy.orm import relationship


class DbGovernorate(Base):
    __tablename__ = 'governorates'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    lat=Column(Float)
    long = Column(Float)
    description = Column(Text)
    image = Column(String(200))
    entity = relationship('DbEntity',back_populates='governorate')


class DbEntity(Base):
    __tablename__= 'entites'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100))
    lat = Column(Float)
    long = Column(Float)
    type = Column(String(50))
    description = Column(Text)
    tel = Column(String(20))
    mobile = Column(String(20))
    page = Column(String(50))
    face = Column(String(100))
    cover_image = Column(String(200))
    image = Column(String(200))
    work_hour = Column(String(100))
    rate = Column(Integer)
    recommend = Column(Integer)
    entertainment = Column(Boolean)
    restorant = Column(Boolean)
    archeological = Column(Boolean)
    sites = Column(Boolean)
    hotels = Column(Boolean)
    Shopping = Column(Boolean)
    Resort = Column(Boolean)
    water = Column(Boolean)
    sport = Column(Boolean)
    track = Column(Boolean)
    governorate_id = Column(Integer,ForeignKey('governorates.id'))
    governorate = relationship(DbGovernorate,back_populates='entity')





