# IMEI Checker Service

Сервис для проверки IMEI устройств с интеграцией Telegram бота и REST API. Позволяет проверять IMEI через Telegram бота или через HTTP API запросы.

## Функциональность

- Проверка валидности IMEI
- Получение информации об устройстве по IMEI через сервис imeicheck.net
- Telegram бот для удобного взаимодействия
- REST API для интеграции
- Белый список пользователей для Telegram бота
- Авторизация по токену для API

## Требования

- Python 3.10+
- pip
- virtualenv (опционально)

## Установка

1. Клонируйте репозиторий:

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
```
Linux/MacOS:
```
source venv/bin/activate
```
Windows:
```
venv\Scripts\activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Настройте переменные окружения:
```bash
# Скопируйте пример конфигурации
cp .env.example .env

# Отредактируйте файл .env, добавив свои значения
nano .env
```

## Конфигурация

1. Настройте параметры в файле `.env`:
   ```env
   # Telegram Bot settings
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   ALLOWED_TELEGRAM_USERS=[123456789,987654321]

   # IMEI Check API settings
   IMEICHECK_API_TOKEN=your_imeicheck_api_token_here
   IMEI_API_URL=https://api.imeicheck.net/v1/checks
   
   # Our API access tokens
   API_ACCESS_TOKENS=["your_api_access_token_here"]
   ```

Где:
   - `TELEGRAM_BOT_TOKEN` - токен вашего Telegram бота
   - `ALLOWED_TELEGRAM_USERS` - список ID пользователей в квадратных скобках
   - `IMEICHECK_API_TOKEN` - токен для сервиса imeicheck.net
   - `IMEI_API_URL` - URL API сервиса проверки IMEI
   - `API_ACCESS_TOKENS` - список токенов для доступа к нашему API в квадратных скобках

2. Получите токен Telegram бота:
   - Напишите @BotFather в Telegram
   - Создайте нового бота командой /newbot
   - Скопируйте полученный токен в конфигурацию

3. Узнайте свой Telegram ID:
   - Напишите @userinfobot в Telegram
   - Добавьте полученный ID в ALLOWED_TELEGRAM_USERS

## Запуск

### Вариант 1: Раздельный запуск (рекомендуется)

1. Запустите API сервер:
```bash
python main.py
```
2. В отдельном терминале запустите Telegram бота:
```bash
python bot_runner.py
```

## Использование

### Telegram Bot

1. Найдите вашего бота в Telegram
2. Отправьте команду /start
3. Отправьте IMEI номер для проверки (например: 356735111052198)


### REST API

#### Проверка работоспособности сервиса:
```bash
curl http://localhost:8000/api/health
```
#### Проверка IMEI:
```bash
curl -X POST "http://localhost:8000/api/check-imei" \
-H "X-API-Token: your-api-token" \
-H "Content-Type: application/json" \
-d '{"imei": "356735111052198"}'
```

## API Документация

После запуска сервера, документация доступна по адресам:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc


## Примеры запросов
### Python
```python
import requests
#Проверка IMEI через API
headers = {
"X-API-Token": "your_api_access_token_here",
"Content-Type": "application/json"
}
data = {
"imei": "356735111052198"
}
response = requests.post(
"http://localhost:8000/api/check-imei",
headers=headers,
json=data
)
print(response.json())
```

## Решение проблем

### Бот не отвечает
1. Проверьте правильность токена бота в .env файле
2. Убедитесь, что ваш Telegram ID добавлен в ALLOWED_TELEGRAM_USERS
3. Проверьте, что бот запущен (python bot_runner.py)
4. Посмотрите логи на наличие ошибок

### API не отвечает
1. Убедитесь, что сервер запущен (python main.py)
2. Проверьте, что токен в заголовке X-API-Token соответствует значению из API_ACCESS_TOKENS
3. Проверьте формат отправляемых данных
4. Убедитесь, что IMEI имеет правильный формат (15 цифр)