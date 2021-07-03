from prometheus_client import Summary, Histogram, generate_latest
from flask import request

STATUS_CODE = "status_code"
PATH = "path"
HTTP_METHOD = "method"


class MetricCollector:
    def observe_myself(self, path, method, status_code, duration):
        self._me.labels(path=path, method=method, status_code=status_code).observe(
            duration
        )

    def observe_db(self, status_code, sql_state, duration):
        self._db.labels(status_code=status_code, sql_state=sql_state).observe(duration)

    def observe_external(self, status_code, duration):
        self._external.labels(status_code=status_code).observe(duration)

    def get_latest(self):
        return generate_latest()

    @staticmethod
    def newCollector(service_name):
        prefix = service_name.replace("-", "_")

        about_me = Summary(
            prefix + "_duration_seconds",
            service_name + " latency request distribution",
            [PATH, HTTP_METHOD, STATUS_CODE],
        )

        about_db = Histogram(
            prefix + "_database_duration_seconds",
            "database latency request distribution",
            [STATUS_CODE, "sql_state"],
            buckets=(0.1, 0.25, 0.5, 0.75, 0.90, 1.0, 2.5),
        )

        about_her = Summary(
            prefix + "_audit_duration_seconds",
            "audit service latency request distribution",
            [STATUS_CODE],
        )

        mc = MetricCollector()
        mc._me = about_me
        mc._db = about_db
        mc._external = about_her
        return mc


def get_collector(name):
    return MetricCollector.newCollector(name)


def instrument_requests(app, collector):
    import time

    def before():
        request.start_time = time.time()

    def after(response):
        if request.path != "/metrics":
            request_latency = time.time() - request.start_time
            collector.observe_myself(
                request.path, request.method, response.status_code, request_latency
            )
        return response

    app.before_request(before)
    app.after_request(after)
