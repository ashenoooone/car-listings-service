Backend: FastAPI + fastapi-users
================================

Этот сервис реализует базовый бэкенд для автообъявлений на FastAPI с аутентификацией через fastapi-users.

### Стек

- FastAPI
- fastapi-users (JWT)
- SQLAlchemy (async) + PostgreSQL
- Alembic (миграции, пока не настроены)

### Установка и запуск локально

```bash
cd backend
poetry install
cp .env.example .env
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

По умолчанию сервис слушает `http://localhost:8000`.

### Основные эндпоинты

- `POST /api/login` — авторизация, возврат JWT (от fastapi-users)
- `GET /api/cars` — защищённый список автомобилей (требует Bearer JWT)

### Пользователи

Регистрация и управление пользователями предоставляются роутерами fastapi-users:

- `POST /api/register`
- `GET /api/users/me`

Сидинг админа и миграции Alembic будут добавлены отдельно.