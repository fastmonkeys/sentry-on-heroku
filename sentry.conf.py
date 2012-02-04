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
try:
    if 'DATABASE_URL' in os.environ:
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
except:
    print "Unexpected error:", sys.exc_info()


# Sentry configuration
# --------------------

SENTRY_KEY = os.environ.get('SENTRY_KEY')

# Set this to false to require authentication
SENTRY_PUBLIC = False

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = int(os.environ.get('PORT', 9000))
