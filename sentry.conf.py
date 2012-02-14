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


# Sentry configuration
# --------------------

SENTRY_KEY = os.environ.get('SENTRY_KEY')

# Set this to false to require authentication
SENTRY_PUBLIC = False

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = int(os.environ.get('PORT', 9000))


# Email configuration
# -------------------

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Disable the default admins (for email)
ADMINS = ()

# Set Sentry's ADMINS to a raw list of email addresses
SENTRY_ADMINS = os.environ.get('ADMINS', '').split(',')
