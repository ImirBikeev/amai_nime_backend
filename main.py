from fastapi import FastAPI
from src.routers.router import router as router_anime

app = FastAPI()


app.include_router(router_anime)