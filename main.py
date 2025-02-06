from fastapi import FastAPI
from app.api.routes import router as api_router
from app.bot.handlers import bot

app = FastAPI(title="IMEI Checker")
app.include_router(api_router, prefix="/api")


# Добавляем обработчик для корректного завершения бота
async def on_shutdown():
    await bot.close()


app.add_event_handler("shutdown", on_shutdown)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
