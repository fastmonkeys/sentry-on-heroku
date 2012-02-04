import os
import urlparse


# Monkeypatches
# --------------

# We have to exclude south from logging, because otherwise database migrations
# fail, when Raven tries to log south, before the necessary tables are created,
# which causes migrations to rollback.

from raven import conf

original_setup_logging = conf.setup_logging


def setup_logging(handler, exclude=['raven', 'gunicorn', 'sentry.errors', 'south']):
    return original_setup_logging(handler, exclude)

conf.setup_logging = setup_logging


# Generic
# -------


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


# Sentry configuration
# --------------------

SENTRY_KEY = os.environ.get('SENTRY_KEY')

# Set this to false to require authentication
SENTRY_PUBLIC = False

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = int(os.environ.get('PORT', 9000))
