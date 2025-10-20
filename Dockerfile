FROM python:3.13

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка poetry
RUN pip install poetry

# Назначение рабочей директории
WORKDIR /employee-task

# Копирование файлов зависимостей
COPY pyproject.toml poetry.lock ./

# Отключаем создание виртуального окружения
RUN poetry config virtualenvs.create false

# Установка зависимостей
RUN poetry install --without dev --no-interaction --no-ansi --no-root

# Копирование всего проекта
COPY . .

# Открытие порта 8000 для взаимодействия с приложением
EXPOSE 8000

# Команды для запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]