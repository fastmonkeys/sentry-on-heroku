import os
import multiprocessing

bind = "0.0.0.0:%s" % os.environ.get('PORT', 9000)
secure_scheme_headers = {'X-FORWARDED-PROTO': 'https'}
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
