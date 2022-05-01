# 参考: https://yusekita.com/detail/1af12648-2f0c-4100-be28-f3be2352232c/
FROM python:3.8.2
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./dockerfiles/django/requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./backend/ ./app