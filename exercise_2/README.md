## Exercise 2

```
# first terminal
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ make start_dev
```

```
# second terminal
$ source .venv/bin/activate
$ pip install -r test_requirements.txt
$ locust -f test_perf/locustfile.py
```
