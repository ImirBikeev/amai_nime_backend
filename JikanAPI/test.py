from aiohttp import ClientSession


class http_client:
	def __init__(self, base_url: str):
		self._session = ClientSession(
			base_url = base_url
		)
		
class jikan_http_client(http_client):
	async def get_anime(self,anime_id: int):
		async with self._session.get(f'/v4/anime/{anime_id}') as response:
			result = await response.json()
			return result["data"]