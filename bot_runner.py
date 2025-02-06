import asyncio
import logging
from app.bot.handlers import dp
from aiohttp import ClientSession

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def main():
    async with ClientSession() as session:  # Используем контекстный менеджер
        try:
            logger.info("Запускаем бота...")
            await dp.start_polling(reset_webhook=True)
        except Exception as e:
            logger.error(f"Ошибка при запуске бота: {e}")
        finally:
            logger.info("Бот остановлен")


if __name__ == "__main__":
    asyncio.run(main())
