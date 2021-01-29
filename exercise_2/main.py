from flask import Flask, Response
from flask import request
import ast
import time

from collector import get_collector, instrument_requests
from prometheus_client import (CollectorRegistry,
                               generate_latest)


def add_routes(app,  collector):
    
    @app.route('/login', methods=['POST'])
    def login():
        return 'success' 

    @app.route('/hello')
    def hello_route():
        return 'hello'

    @app.route('/world')
    def world_route():
        return 'world'

    @app.route('/order', methods=['POST'])
    def order():
        # getting data from db
        try:
            save_order(collector)
        except RuntimeError as re:
            r = Response('{0}'.format(re), mimetype='text/plain')
            r.status_code = 503
            return r

        # calling an external service
        try:
            order_delivery(collector)
        except RuntimeError as re:
            r = Response('{0}'.format(re), mimetype='text/plain')
            r.status_code = 503
            return r
        return 'Success!'


def save_order(collector):
    start_time = time.time()

    db_sleep = float(request.args.get('db_sleep', 0))
    is_db_error = ast.literal_eval(request.args.get('is_db_error', 'False'))

    try:
        call_db(db_sleep, is_db_error)
        latency = time.time() - start_time
        collector.observe_db('0', '0', latency)
    except RuntimeError as re:
        """
        """
        latency = time.time() - start_time
        collector.observe_db('1001', 'HY000', latency)
        raise re


def call_db(db_sleep, is_error):
    mocked_call("Database XYZ", db_sleep, is_error)


def order_delivery(collector):
    start_time = time.time()
    srv_sleep = float(request.args.get('srv_sleep', 0))
    is_srv_error = ast.literal_eval(request.args.get('is_srv_error', 'False'))

    try:
        call_external(srv_sleep, is_srv_error)
        latency = time.time() - start_time
        collector.observe_external('200', latency)
    except RuntimeError as re:
        """
        """
        latency = time.time() - start_time
        collector.observe_external('500', latency)
        raise re


def call_external(srv_sleep, is_error):
    mocked_call('Service Audit', srv_sleep, is_error)


def mocked_call(what, sleep, is_error):
    if sleep > 0:
        time.sleep(sleep)
    if is_error:
        raise RuntimeError(what + ' failed to process request')


def add_metrics_route(app, collector):
    @app.route('/metrics', strict_slashes=False, methods=['GET'])
    def metrics_rotue():
        txt = generate_latest()
        return Response(txt, mimetype='text/plain')


def get_app():
    app = Flask(__name__)
    c = get_collector('order-mgmt')
    add_routes(app, c)
    add_metrics_route(app, c)
    instrument_requests(app, c)
    return app


if __name__ == '__main__':
    app = get_app()
    app.run(host='0.0.0.0',
            port=8080)
