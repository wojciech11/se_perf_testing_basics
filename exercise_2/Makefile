start_dev:
	python main.py

start_with_gunicorn:
	gunicorn --bind 0.0.0.0:8080 -w 1 wsgi:app

srv_random_trafic:
	curl 127.0.0.1:8080/hello ; \
	curl 127.0.0.1:8080/world ;

srv_random_trafic_complex_failed_db:
	curl 127.0.0.1:8080/complex?is_db_error=True

srv_random_trafic_complex_slow_db_and_svc:
	curl '127.0.0.1:8080/complex?db_sleep=3&srv_sleep=2'

srv_random_trafic_complex_failed_third_party:
	curl '127.0.0.1:8080/complex?is_srv_error=True'

locust:
	locust -f test_perf/locustfile.py