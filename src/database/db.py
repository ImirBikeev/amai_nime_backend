from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
class UserDB(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    disabled = Column(Boolean, default=False)