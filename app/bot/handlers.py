import logging
from aiogram import Bot, Dispatcher, types
from ..core.config import settings
from ..core.imei_validator import IMEIValidator
from ..core.imei_service import IMEIService

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    logger.info(f"Получена команда start от пользователя {message.from_user.id}")
    await message.reply("Привет! Отправь мне IMEI для проверки.")


@dp.message_handler()
async def check_imei(message: types.Message):
    logger.info(
        f"Получено сообщение от пользователя {message.from_user.id}: {message.text}"
    )

    if message.from_user.id not in settings.ALLOWED_TELEGRAM_USERS:
        logger.warning(
            f"Попытка доступа от неразрешенного пользователя {message.from_user.id}"
        )
        await message.reply("У вас нет доступа к этому боту.")
        return

    imei = message.text.strip()

    if not IMEIValidator.is_valid(imei):
        logger.info(f"Неверный формат IMEI: {imei}")
        await message.reply(
            "Неверный формат IMEI. Пожалуйста, проверьте номер. Пример правильного ввода: 356735111052198"
        )
        return

    imei_service = IMEIService()
    try:
        logger.info(f"Отправляем запрос на проверку IMEI: {imei}")
        result = await imei_service.check_imei(imei)
        formatted_result = f"🔍 Результат проверки IMEI: {imei}\n\n{result}"
        await message.reply(formatted_result)
    except Exception as e:
        logger.error(f"Ошибка при проверке IMEI: {e}")
        await message.reply("Произошла ошибка при проверке IMEI.")
