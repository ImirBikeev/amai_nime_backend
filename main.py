from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Annotated, Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.routers.router import router as router_anime
from src.auth.router import router as auth_router

app = FastAPI()


# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_anime)
app.include_router(auth_router)
