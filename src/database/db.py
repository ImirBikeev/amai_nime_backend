from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATADASE=""

engine = create_engine(URL_DATABASE)

Sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()