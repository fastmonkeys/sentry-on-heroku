import os
import sys
import urlparse

from sentry.conf.server import *

ROOT = os.path.dirname(__file__)

sys.path.append(ROOT)


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
SENTRY_WEB_OPTIONS = {
    'workers': 8,
    'worker_class': 'gevent',
}


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

# The threshold level to restrict emails to.
SENTRY_MAIL_LEVEL = logging.WARNING

# The prefix to apply to outgoing emails.
SENTRY_EMAIL_SUBJECT_PREFIX = '[Sentry] '

# The reply-to email address for outgoing mail.
SENTRY_SERVER_EMAIL = os.environ.get('SERVER_EMAIL', 'root@localhost')


# SSL configuration
# -----------------

# Force secure connection.
HTTPS_REQUIRED = 'HTTPS_REQUIRED' in os.environ

# Whether to use a secure cookie for the session cookie.  If this is set to
# `True`, the cookie will be marked as "secure," which means browsers may
# ensure that the cookie is only sent under an HTTPS connection.
SESSION_COOKIE_SECURE = True

MIDDLEWARE_CLASSES += ('middleware.SSLMiddleware',)
