import logging
import os
import sys

from sentry.conf.server import *

ROOT = os.path.dirname(__file__)

sys.path.append(ROOT)

import dj_database_url
DATABASES = {'default': dj_database_url.config()}


# Sentry configuration
# --------------------

SENTRY_KEY = os.environ.get('SENTRY_KEY')

# Set this to false to require authentication
SENTRY_PUBLIC = False

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = int(os.environ.get('PORT', 9000))
SENTRY_WEB_OPTIONS = {
    'workers': 3,
    'worker_class': 'gevent',
}

SENTRY_URL_PREFIX = os.environ.get('SENTRY_URL_PREFIX', '')


# Email configuration
# -------------------

if 'SENDGRID_USERNAME' in os.environ:
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
    EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
elif 'MANDRILL_USERNAME' in os.environ:
    EMAIL_HOST = 'smtp.mandrillapp.com'
    EMAIL_HOST_USER = os.environ.get('MANDRILL_USERNAME')
    EMAIL_HOST_PASSWORD = os.environ.get('MANDRILL_APIKEY')

EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Disable the default admins (for email)
ADMINS = ()

# Set Sentry's ADMINS to a raw list of email addresses
SENTRY_ADMINS = os.environ.get('ADMINS', '').split(',')

# The threshold level to restrict emails to.
SENTRY_MAIL_LEVEL = logging.WARNING

# The prefix to apply to outgoing emails.
EMAIL_SUBJECT_PREFIX = '[Sentry] '

# The reply-to email address for outgoing mail.
SERVER_EMAIL = os.environ.get('SERVER_EMAIL', 'root@localhost')

DEFAULT_FROM_EMAIL = os.environ.get(
    'DEFAULT_FROM_EMAIL',
    'webmaster@localhost'
)


# Security
# --------

INSTALLED_APPS += ('djangosecure',)
MIDDLEWARE_CLASSES += ('djangosecure.middleware.SecurityMiddleware',)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Whether to use HTTPOnly flag on the session cookie. If this is set to `True`,
# client-side JavaScript will not to be able to access the session cookie.
SESSION_COOKIE_HTTPONLY = True

# Whether to use a secure cookie for the session cookie.  If this is set to
# `True`, the cookie will be marked as "secure," which means browsers may
# ensure that the cookie is only sent under an HTTPS connection.
SESSION_COOKIE_SECURE = True

# If set to `True`, causes `SecurityMiddleware` to set the
# `X-Content-Type-Options: nosniff` header on all responses that do not already
# have that header.
SECURE_CONTENT_TYPE_NOSNIFF = True

# If set to `True`, causes `SecurityMiddleware` to set the
# `X-XSS-Protection: 1; mode=block` header on all responses that do not already
# have that header.
SECURE_BROWSER_XSS_FILTER = True

# If set to `True`, causes `SecurityMiddleware` to set the `X-Frame-Options:
# DENY` header on all responses that do not already have that header
SECURE_FRAME_DENY = True

# If set to a non-zero integer value, causes `SecurityMiddleware` to set the
# HTTP Strict Transport Security header on all responses that do not already
# have that header.
SECURE_HSTS_SECONDS = 31536000

# If `True`, causes `SecurityMiddleware` to add the ``includeSubDomains`` tag
# to the HTTP Strict Transport Security header.
#
# Has no effect unless ``SECURE_HSTS_SECONDS`` is set to a non-zero value.
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# If set to True, causes `SecurityMiddleware` to redirect all non-HTTPS
# requests to HTTPS
SECURE_SSL_REDIRECT = True


# Bcrypt
# ------

INSTALLED_APPS += ('django_bcrypt',)

# Enables bcrypt password migration on a ``check_password()`` call.
#
# The hash is also migrated when ``BCRYPT_ROUNDS`` changes.
BCRYPT_MIGRATE = True


# Social Auth
# -----------

SOCIAL_AUTH_CREATE_USERS = 'SOCIAL_AUTH_CREATE_USERS' in os.environ


# Twitter
# -------
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')


# Facebook
# --------

FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
FACEBOOK_API_SECRET = os.environ.get('FACEBOOK_API_SECRET')


# Google
# ------

GOOGLE_OAUTH2_CLIENT_ID = os.environ.get('GOOGLE_OAUTH2_CLIENT_ID')
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET')


# GitHub
# ------

GITHUB_APP_ID = os.environ.get('GITHUB_APP_ID')
GITHUB_API_SECRET = os.environ.get('GITHUB_API_SECRET')
GITHUB_EXTENDED_PERMISSIONS = ['repo']


# Bitbucket
# ---------

BITBUCKET_CONSUMER_KEY = os.environ.get('BITBUCKET_CONSUMER_KEY')
BITBUCKET_CONSUMER_SECRET = os.environ.get('BITBUCKET_CONSUMER_SECRET')
