Sentry on Heroku
================

    Sentry_ is a realtime event logging and aggregation platform.  At its core
    it specializes in monitoring errors and extracting all the information
    needed to do a proper post-mortem without any of the hassle of the
    standard user feedback loop.

    .. _Sentry: https://github.com/getsentry/sentry


Quick setup
-------------

Click the button below to automatically set up the Sentry in an app running on
your Heroku account.

.. image:: https://www.herokucdn.com/deploy/button.png
   :target: https://heroku.com/deploy
   :alt: Deploy

Finally, you need to setup your first user::

    heroku run "sentry --config=sentry.conf.py createsuperuser" --app YOURAPPNAME


Manual setup
-------------

Follow the steps below to get Sentry up and running on Heroku:

1. Create a new Heroku application. Replace "APP_NAME" with your
   application's name::

        heroku apps:create APP_NAME

2. Add database to the application::

        heroku addons:create heroku-postgresql:dev
        heroku pg:promote $(heroku config -s | awk -F= '$1 ~ /^HEROKU_POSTGRESQL_[A-Z]+_URL$/ {print $1}' | sed 's/_URL$//')

3. Set the Django settings module to be used::

        heroku config:set DJANGO_SETTINGS_MODULE=sentry.conf

4. Set Django's secret key for cryptographic signing and Sentry's shared secret
   for global administration privileges::

        heroku config:set SECRET_KEY=$(python -c "import base64, os; print(base64.b64encode(os.urandom(40)).decode())")
        heroku config:set SENTRY_KEY=$(python -c "import base64, os; print(base64.b64encode(os.urandom(40)).decode())")

5. Set the absolute URL to the Sentry root directory. The URL should not include
   a trailing slash. Replace the URL below with your application's URL::

        heroku config:set SENTRY_URL_PREFIX=https://sentry-example.herokuapp.com

6. Deploy Sentry to Heroku::

        git push heroku master

7. Run Sentry's database migrations::

        heroku run "sentry --config=sentry.conf.py upgrade"

8. Create a user account for yourself::

        heroku run "sentry --config=sentry.conf.py createsuperuser"

That's it!


Email notifications
-------------------

Follow the steps below, if you want to enable Sentry's email notifications:

1. Add either SendGrid or Mandrill add-on to your Heroku application::

        heroku addons:create sendgrid

   or::

        heroku addons:create mandrill

2. Set the reply-to email address for outgoing mail::

        heroku config:set SERVER_EMAIL=sentry@example.com

3. Set the email addresses that should be notified::

        heroku config:set ADMINS=john.matrix@example.com,jack.daniels@example.com


Version notes
-------------------

The version of Sentry pinned in the ``requirements.txt`` file is one of the last for which Redis was not a hard dependency. Newer versions of Sentry will not work on Heroku using this configuration as Redis is required.

Note that if you are sending events from raven (e.g. in Django) to an installation of Sentry provided by this repo, you will need to pin the raven version to ``5.0.0`` otherwise you will get errors about mismatched protocols.

You may also need to add a ``?timeout=`` parameter to your DSN URL in Django, or messages to Sentry may time out. Values of 3 seconds and up seem to work fine.

