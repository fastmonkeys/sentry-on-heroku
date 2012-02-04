import os
import urlparse

from sentry.conf.server import *

ROOT = os.path.dirname(__file__)


# Database configuration
# ----------------------
#
# See: http://devcenter.heroku.com/articles/django#postgres_database_config

urlparse.uses_netloc.append('postgres')
urlparse.uses_netloc.append('mysql')

url = urlparse.urlparse(os.environ['DATABASE_URL'])
engines = {
    'postgres': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}
DATABASES = {
    'default': {
        'ENGINE': engines[url.scheme],
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
}


# Logging
# -------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'south': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'DEBUG',
        },
    },
}


# Sentry configuration
# --------------------

SENTRY_KEY = os.environ.get('SENTRY_KEY')

# Set this to false to require authentication
SENTRY_PUBLIC = False

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = int(os.environ.get('PORT', 9000))
