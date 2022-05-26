from sqlalchemy import Column, Integer, String

from models.base import Base

convention ={
    "pk": "pk_%(table_name)s"
}

class Address(Base):
    __tablename__='address'

    id= Column(Integer, primary_key=True)
    permanent_addr = Column(String(100))
    temporary_addr = Column(String(100))
    fake_addr= Column(String(100))
    
class Family(Base):
    __tablename__='family'

    id= Column(Integer, primary_key=True)
    permanent_addr = Column(String(100))
    temporary_addr = Column(String(100))