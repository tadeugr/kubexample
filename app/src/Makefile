.PHONY: start start-dev
start:
	gunicorn --bind 0.0.0.0:5000 --log-level DEBUG wsgi:app

start-dev:
	python3 kubexample.py