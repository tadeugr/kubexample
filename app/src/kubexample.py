# Import required modules
import os
import logging
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Setup routes
@app.route('/')
def home():
    return 'Hello, home!'

@app.route('/health')
def health():
    return 'Hello, health!'

@app.route('/ready')
def ready():
    return 'Hello, ready!'

@app.route('/payload')
def payload():
    return 'Hello, payload!'

@app.route('/metrics')
def metrics():
    return 'Hello, metrics!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')