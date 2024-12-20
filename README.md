# WeatherBot 🌤️

**WeatherBot** — это телеграм-бот, который предоставляет информацию о текущей погоде, прогнозе на 5 дней, а также позволяет настроить уведомления о погоде.

---

## 🚀 Функционал

- **Текущая погода**: Узнайте температуру, влажность, скорость ветра и описание погоды для выбранного города.
- **Прогноз на 5 дней**: Получите подробный прогноз погоды на ближайшие 5 дней.
- **Уведомления о погоде**: Настройте ежедневные уведомления о погоде в выбранное вами время.
- **Удобный интерфейс**: Используйте кнопки для навигации, без необходимости вводить команды.

---

## 📦 Установка и запуск

### Шаг 1: Клонируйте репозиторий
```bash
git clone https://github.com/username/weather-bot.git
cd weather-bot
```
### Шаг 2: Установите зависимости
Убедитесь, что у вас установлен Python 3.9+.
```bash
pip install -r requirements.txt
```
### Шаг 3: Настройте переменные окружения
Создайте файл `.env` в корневой папке проекта и добавьте в него следующие переменные:
```env
BOT_TOKEN=your_telegram_bot_token
API_KEY=your_openweathermap_api_key
```
### Шаг 4: Запустите бота
```bash
python main.py
```

## 🛠️ Используемые технологии
- aiogram — фреймворк для создания телеграм-ботов.
- Aiohttp — библиотека для выполнения HTTP-запросов.
- APScheduler — для настройки задач по расписанию.
- OpenWeather API — для получения данных о погоде.

## 🧑‍💻 Как пользоваться ботом?
После запуска бота, доступны следующие действия:
  1. Узнать текущую погоду: Нажмите кнопку "Узнать погоду в выбранном городе", введите название города.
  2. Прогноз на 5 дней: Нажмите кнопку "Прогноз погоды на 5 дней", введите название города.
  3. Уведомления: Нажмите кнопку "Установить уведомление о погоде" и настройте время.

## 📂 Структура проекта
```bash
weather-bot/
├── main.py                # Основной файл для запуска бота
├── router.py              # Маршруты и обработчики событий
├── service.py             # Функции для получения данных о погоде
├── requirements.txt       # Список зависимостей
├── .env                   # Переменные окружения
└── README.md              # Документация
```

## 🔧 Возможные доработки
- Добавить больше языков для взаимодействия с пользователем.
- Реализовать уведомления с прогнозом на неделю.
- Добавить поддержку геолокации для определения погоды.
