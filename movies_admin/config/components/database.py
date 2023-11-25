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

CONN_MAX_AGE = 30

LOGGING = MappingProxyType({
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s: %(message)s ' +
            '[in %(pathname)s:%(lineno)d]',
        },
    },
    'handlers': {
        'debug-console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['require_debug_true'],
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['debug-console'],
            'propagate': False,
        },
    },
})
