FROM python:3.10-slim-buster

# Install required build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libdbus-1-dev \
    libgirepository1.0-dev \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    libpq-dev \
    dbus \
    gir1.2-glib-2.0

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn --bind 0.0.0.0:$PORT codestar.wsgi:application