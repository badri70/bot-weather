from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from service import get_weather, get_weather_forecast


router = Router()
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Узнать погоду в выбранном городе')],
        [KeyboardButton(text='Установить уведомление о погоде')],
        [KeyboardButton(text='Прогноз погоды на 5 дней')],
        [KeyboardButton(text='Узнать все команды')]
    ],
    resize_keyboard=True
)


class WeatherState(StatesGroup):
    city = State()
    forecast = State()


class NotificationState(StatesGroup):
    city = State()


user_notifications = {}


@router.message(lambda message: message.text == 'Установить уведомление о погоде')
async def set_notification_city(message: Message, state: FSMContext):
    await message.answer("Введите название города, для которого вы хотите получать уведомления о погоде.")
    await state.set_state(NotificationState.city)


@router.message(NotificationState.city)
async def save_notification_city(message: Message, state: FSMContext):
    city_name = message.text.strip()
    user_notifications[message.from_user.id] = city_name  # Сохраняем город для пользователя
    await message.answer(
        f"Уведомления о погоде для города {city_name.title()} успешно настроены! 🔔",
        reply_markup=keyboard
    )
    await state.clear()


async def send_weather_notification():
    for user_id, city in user_notifications.items():
        weather_text = await get_weather(city)  # Получаем текущую погоду для города
        try:
            await router.bot.send_message(user_id, f"Ежедневное уведомление о погоде для города {city.title()}:\n\n{weather_text}")
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")


@router.message(CommandStart())
async def start(message: Message):
    welcome_text = (
        "Привет! 👋\n\n"
        "Я — ваш бот-помощник для проверки погоды! ☀️🌧\n"
        "С моей помощью вы можете узнать:\n\n"
        "🌡 Текущую температуру, влажность и ветер в любом городе.\n"
        "📅 Прогноз погоды на несколько дней вперед.\n"
        "🔔 Настроить уведомления о погоде.\n"
        "📍 Быстро узнать погоду для вашего местоположения или в inline-режиме.\n\n"
        "Выберите одну из кнопок в меню, чтобы начать:\n"
        "- Узнать погоду в выбранном городе\n"
        "- Прогноз погоды на 5 дней\n"
        "- Установить уведомление о погоде\n"
        "- Узнать все команды"
    )
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=keyboard)


@router.message(lambda message: message.text == 'Узнать погоду в выбранном городе')
async def weather(message: Message, state: FSMContext):
    await message.answer('Пожалуйста, введите название города, чтобы я мог узнать погоду для вас.')
    await state.set_state(WeatherState.city)


@router.message(WeatherState.city)
async def fetch_current_weather(message: Message, state: FSMContext):
    city_name = message.text.strip()
    if not city_name:
        await message.answer("Пожалуйста, укажите название города после команды. Пример: `/weather Москва`")
        return

    weather_text = await get_weather(city_name)
    await message.answer(weather_text)
    await state.clear()


@router.message(lambda message: message.text == 'Прогноз погоды на 5 дней')
async def forecast(message: Message, state: FSMContext):
    await message.answer('Пожалуйста, введите название города, чтобы я мог узнать погоду для вас.')
    await state.set_state(WeatherState.forecast)


@router.message(WeatherState.forecast)
async def fetch_forecast_weather(message: Message, state: FSMContext):
    city_name = message.text.strip()
    if not city_name:
        await message.answer("Пожалуйста, укажите название города после команды. Пример: `/weather Москва`")
        return

    weather_text = await get_weather_forecast(city_name)
    await message.answer(weather_text)
    await state.clear()


@router.message(lambda message: message.text == 'Узнать все команды')
async def show_commands(message: Message):
    commands_text = (
        "Вот доступные функции бота:\n\n"
        "- Узнать погоду в выбранном городе 🌡\n"
        "- Прогноз погоды на 5 дней 📅\n"
        "- Установить уведомление о погоде 🔔\n"
        "Выберите соответствующую кнопку в меню, чтобы воспользоваться функцией."
    )
    await message.answer(commands_text)
