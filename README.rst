Sentry on Heroku
================

    Sentry_ is a realtime event logging and aggregation platform.  At its core
    it specializes in monitoring errors and extracting all the information
    needed to do a proper post-mortem without any of the hassle of the
    standard user feedback loop.

    .. _Sentry: https://github.com/dcramer/sentry


Basic setup
-----------

Follow the steps below to get Sentry up and running on Heroku:

1. Create a new Heroku application. Replace "APP_NAME" with your
   application's name::

        heroku apps:create --stack cedar APP_NAME

2. Add database to the application::

        heroku addons:add shared-database

3. Set Sentry's shared secret for global administration privileges::

        heroku config:add SENTRY_KEY='0123456789abcde'

   You may use the following Python code to generate a good unique key for
   the above::

       >>> import base64
       >>> import os
       >>> base64.b64encode(os.urandom(40))
       'nIumxPtjDuHunpX2D+LP27l8WX967DgjBRiSLz/XrfAp491bu3pnzw=='

4. Force SSL, in order to use secure cookies::

        heroku config:add HTTPS_REQUIRED=1

5. Deploy Sentry to Heroku::

        git push heroku master

6. Run Sentry's database migrations::

        heroku run "sentry --config=sentry.conf.py upgrade"

7. Create a user account for yourself::

        heroku run "sentry --config=sentry.conf.py createsuperuser"

That's it!


Email notifications
-------------------

Follow the steps below, if you want to enable Sentry's email notifications:

1. Add SendGrid add-on to your Heroku application::

        heroku addons:add sendgrid

2. Set the reply-to email address for outgoing mail::

        heroku config:add SERVER_EMAIL=sentry@example.com

3. Set the email addresses that should be notified::

        heroku config:add ADMINS=john.matrix@example.com,jack.daniels@example.com


