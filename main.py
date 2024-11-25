import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from router import router
from router import send_weather_notification


load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()
scheduler = AsyncIOScheduler()


async def setup_scheduler():
    """
    Настройка и запуск задач планировщика.
    """
    scheduler.add_job(
        send_weather_notification,  # Функция для выполнения
        trigger="cron",             # Запуск по расписанию
        hour=9,                     # В 9 утра
        minute=0
    )
    scheduler.start()


async def main():
    dp.include_router(router=router)
    await setup_scheduler()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main=main())

