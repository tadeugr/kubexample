# Start production server
start:
	gunicorn --bind 0.0.0.0:5000 --log-level DEBUG wsgi:app

# Start dev server
start-dev:
	python3 kubexample.py