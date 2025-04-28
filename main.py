from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.routers.router import router as router_anime
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

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


app.include_router(router_anime)
