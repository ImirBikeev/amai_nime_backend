from fastapi import APIRouter
from JikanAPI.test import jikan_http_client

api_client = jikan_http_client(base_url="https://api.jikan.moe")

router = APIRouter(
	prefix='/api'
)

@router.get("")
async def get_anime():
		return await "a"


@router.get("/get_anime/{anime_id}")
async def get_anime(anime_id: int):
		return await api_client.get_anime(anime_id)	