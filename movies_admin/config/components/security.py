"""Security settings."""

import os

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = os.getenv('DEBUG', default=False) == 'True'

ALLOWED_HOSTS = ('127.0.0.1', 'localhost')

CORS_ALLOWED_ORIGINS = ('http://127.0.0.1', 'http://127.0.0.1:8080')
