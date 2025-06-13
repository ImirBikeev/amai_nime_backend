from sqlalchemy.orm import Session
from passlib.context import CryptContext
from amai_nime_backend import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    return db.query(models.UserDB).filter(models.UserDB.username == username).first()

def create_user(db: Session, user: models.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.UserDB(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user