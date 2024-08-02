from mubble.client import AiohttpClient
from src.config import BOT_TOKEN

http_client = AiohttpClient()


async def download_file(file_path: str) -> bytes:
    response = await http_client.request_content(
        f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
    )
    return response
