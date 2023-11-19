#!/usr/bin/env bash

python manage.py collectstatic --noinput \
&& python manage.py migrate movies initial0001 --fake \
&& python manage.py migrate

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi
python sqlite_to_postgres/main.py
uwsgi --strict --ini uwsgi.ini