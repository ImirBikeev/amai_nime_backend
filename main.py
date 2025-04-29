from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.routers.router import router as router_anime
from pydantic import BaseModel
from typing import List, Annotated
from authx import AuthX, AuthXConfig

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_acess_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = Auth(config=config)

class User_Base(BaseModel):
  user_name: str
  user_id: int


origins = [
  "*"
]  

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login():
  pass

@app.get("/protected")
async def protected():
  pass


app.include_router(router_anime)
