"""Database connection settings."""

import os
from types import MappingProxyType

DATABASE_PORT = 5432

DATABASES = MappingProxyType({
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', DATABASE_PORT),
        'OPTIONS': {
            'options': '-c search_path={db_schemas}'.format(
                db_schemas=os.getenv('DB_SCHEMAS'),
            ),
        },
    },
})

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
