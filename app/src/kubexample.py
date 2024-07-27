# Flask webserver

# Import required modules
import os
import logging
import asyncio
import random
from flask import Flask, request, jsonify, make_response
from prometheus_flask_exporter import PrometheusMetrics

# Setup logging
logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])
logger = logging.getLogger()

# Setup Flas app
app = Flask(__name__)

# Create prometheus middleware
metrics = PrometheusMetrics(app)
# static information as metric
metrics.info('app_info', 'Application info', version='0.0.1')

# Find Nth number in Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return "ERROR: n must be > 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Setup routes

# Home (root)
@app.route('/')
def home():
    return 'Hello, home!'

# Liveness probe endpoint
@app.route('/health')
def health():
    data = {'status': 'healthy'}
    return make_response(jsonify(data), 200)

# Readiness probe endpoint
@app.route('/ready')
def ready():
    data = {'status': 'ready'}
    return make_response(jsonify(data), 200)

# Async Fibonacci function
@app.route('/payload')
async def payload():
    # Create a random integer
    n = random.randint(1, 10)

    # Call fibonacci funcation asynchronously
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, fibonacci, n)

    data = {'n': n, 'fibonacci' : result}
    return make_response(jsonify(data), 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0')