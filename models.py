from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from db import Base

class Users(Base):
    __tablename__ = 'profile'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)