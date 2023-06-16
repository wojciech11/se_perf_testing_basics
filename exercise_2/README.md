## Exercise 2

```bash
# first terminal
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ make start_dev
```

```bash
# second terminal
$ source .venv/bin/activate
$ pip install -r test_requirements.txt
$ locust -f test_perf/locustfile.py
```

Next open http://127.0.0.1:8089/ and start tests. After 4-5 minutes examine 127.0.0.1:8080/metrics (Prometheus).

### Materiały

- [Grafana przykładowy dashboard z metrykami](https://play.grafana.org/d/000000109/the-four-golden-signals?orgId=1)

#### Dodatkowe:

- [Grafana najlepsze praktyki](https://grafana.com/docs/grafana/latest/best-practices/common-observability-strategies/#the-four-golden-signals)
- [Prezentacja o monitoringu z Prometheusem wraz z przykładami aplikacji Py/Go/Java](https://github.com/wojciech12/talk_monitoring_with_prometheus)
