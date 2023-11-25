FROM python:3.11-slim-bookworm
LABEL developer="Patrushev Sergey, email: <PatrushevSergeyVal@yandex.ru>"

ARG POETRY_VERSION

WORKDIR /opt/app

RUN apt update -y && apt install -y gcc
RUN apt install -y gettext

RUN mkdir /opt/app/static && mkdir /opt/app/media
RUN groupadd -r admin_panel && useradd -d /opt/app -r -g admin_panel web && chown web:admin_panel -R /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV UWSGI_PROCESSES 4
ENV UWSGI_THREADS 8
ENV UWSGI_HARAKIRI 60

ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY uwsgi.ini uwsgi.ini

RUN  mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && pip install --upgrade pip \
     && pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction

COPY . .
RUN chmod u+x start.sh

EXPOSE 8000

USER web

CMD ["./start.sh"]
