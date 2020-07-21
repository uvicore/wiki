# Starlette Hello World
**p53 38342 req/sec**
```
$ gunicorn -w 8 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:5000 hello:app
$ wrk -c1000 -t4 -d30 http://localhost:5000/
Running 30s test @ http://localhost:5000/
  4 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    27.13ms   16.75ms 230.31ms   80.06%
    Req/Sec     9.67k     2.80k   20.80k    70.74%
  1153897 requests in 30.09s, 156.26MB read
Requests/sec:  38342.07
Transfer/sec:      5.19MB
```


# Starlette Database Query
**p53 3358 req/sec**
```
$ gunicorn -w 8 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:5000 database:app
$ wrk -c1000 -t4 -d30 http://localhost:5000/users
Running 30s test @ http://localhost:5000/users
  4 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   325.01ms  256.52ms   1.86s    76.22%
    Req/Sec   847.10    443.18     2.58k    70.21%
  100866 requests in 30.04s, 17.03MB read
Requests/sec:   3358.00
Transfer/sec:    580.44KB
```


# Uvicore Hello World
**p53 7288 req/sec**
```
$ gunicorn -w 8 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:5000 mreschke.wiki.http.server:http
$ wrk -c1000 -t4 -d30 http://localhost:5000/about
Running 30s test @ http://localhost:5000/about
  4 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   143.42ms   92.38ms 784.97ms   75.39%
    Req/Sec     1.84k     0.94k    4.47k    68.06%
  218958 requests in 30.04s, 29.44MB read
Requests/sec:   7288.22
Transfer/sec:      0.98MB
```


# Flask Framework Hello World
**p53 4281 req/sec**
```
$ gunicorn -w 8 -b 127.0.0.1:5000 server:app
$ wrk -c1000 -t4 -d30 http://localhost:5000/v1/ping
Running 30s test @ http://localhost:5000/v1/ping
  4 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   231.13ms   57.32ms 455.20ms   60.53%
    Req/Sec     1.08k   327.31     2.05k    65.66%
  128863 requests in 30.10s, 19.42MB read
Requests/sec:   4281.16
Transfer/sec:    660.57KB
```


# Flask Framework Database Query
**p53 1256 req/sec**
```
$ gunicorn -w 8 -b 127.0.0.1:5000 server:app
$ wrk -c1000 -t4 -d30 http://localhost:5000/v1/users
Running 30s test @ http://localhost:5000/v1/users
  4 threads and 1000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   782.76ms  151.11ms   1.42s    92.50%
    Req/Sec   316.87     87.78   585.00     75.23%
  37762 requests in 30.08s, 10.23MB read
Requests/sec:   1255.51
Transfer/sec:    348.21KB
```
