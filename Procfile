web: uwsgi --ini=uwsgi.ini --http=0.0.0.0:$PORT
worker: sentry --config=sentry.conf.py celery worker --loglevel=INFO
beat: sentry --config=sentry.conf.py celery beat --loglevel=INFO
