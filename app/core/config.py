from typing import List
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()


class Settings(BaseSettings):
    # API настройки для imeicheck.net
    IMEICHECK_API_TOKEN: str
    IMEI_API_URL: str = "https://api.imeicheck.net/v1/checks"

    # Telegram настройки
    TELEGRAM_BOT_TOKEN: str
    ALLOWED_TELEGRAM_USERS: List[int]

    # Токены для доступа к нашему API
    API_ACCESS_TOKENS: List[str]

    # Используем новый способ конфигурации через ConfigDict
    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
