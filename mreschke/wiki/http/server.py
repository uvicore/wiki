import os
from ..support import bootstrap
from fastapi import FastAPI

# Bootstrap the Uvicore application
app = bootstrap.application(is_console=False)

# Http entrypoint for uvicorn or gunicorn
# uvicorn --port 5000 mreschke.wiki.http.server:http --reload
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:5000 mreschke.wiki.http.server:http
http = app.http.server


# Import main app router
#from .routes import routes
#routes(http)

# https://github.com/borislemke/nodejs_vs_php
# On mac mini = 53322 req/sec
# gunicorn -w 8 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:5000 mreschke.wiki.http.server:http
# wrk -c5000 -t10 -d30 http://localhost:5000/hello
# Running 30s test @ http://localhost:5000/hello
#   10 threads and 5000 connections
#   Thread Stats   Avg      Stdev     Max   +/- Stdev
#     Latency     4.50ms    2.35ms  49.17ms   72.99%
#     Req/Sec     5.97k     4.81k   16.57k    66.96%
#   1605036 requests in 30.10s, 217.36MB read
#   Socket errors: connect 4759, read 63, write 13, timeout 0
# Requests/sec:  53322.42
# Transfer/sec:      7.22MB

# Stock starlette, hello world same gunicork -w 8
# On sunmacn 18.16k req/sec
# On p53 4.14k req/sec

# Stock starlette, databases[mysql], query Users table that has 2 entries, id,name
# On p53, 555 req/sec, but there were 3990 socket connection errors and 598 timeouts

# My Sunfinity Python Flask Framework
# Larger users table, returning ID, Email, Name for 25 records
# gunicorn -w 8 -b 127.0.0.1:5000 server:app
# On p53, 120 req/sec but also get 3990 soecket connection errors
# If I lower to -c200 -t10 -d10 I get 130 req/sec with no errors
# Guessing MySQL is erroring

