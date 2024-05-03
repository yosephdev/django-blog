FROM python:3.10-slim-buster

# Install required build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libdbus-1-dev \
    libgirepository1.0-dev \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    libpq-dev

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir psycopg2-binary
RUN pip install django dj_database_url django_summernote whitenoise gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "codestar.wsgi:application"]

