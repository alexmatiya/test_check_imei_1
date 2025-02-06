from typing import Dict, Any
from aiohttp import ClientSession
from .config import settings


class IMEIService:
    def __init__(self) -> None:
        self.api_url: str = settings.IMEI_API_URL
        self.api_token: str = settings.IMEICHECK_API_TOKEN

    async def check_imei(self, imei: str) -> Dict[str, Any]:
        async with ClientSession() as session:  # Используем контекстный менеджер
            headers = {
                "Authorization": f"Bearer {self.api_token}",
                "Content-Type": "application/json",
            }
            data = {"deviceId": imei, "serviceId": 12}
            async with session.post(
                self.api_url, headers=headers, json=data
            ) as response:
                return await response.json()
