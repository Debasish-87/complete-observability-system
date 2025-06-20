from flask import Flask
import logging
import time

from prometheus_client import Counter, Summary, generate_latest, CONTENT_TYPE_LATEST
from flask_opentracing import FlaskTracing
from jaeger_client import Config

# Initialize Flask App
app = Flask(__name__)

# Setup Logging
logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.INFO
)

# Setup Prometheus Metrics
REQUEST_COUNT = Counter(
    "http_requests_total", "Total HTTP Requests",
    ["method", "endpoint"]
)
REQUEST_LATENCY = Summary(
    "http_request_latency_seconds", "Request latency"
)

# Setup Jaeger Tracing
def init_tracer(service_name='flask-observability'):
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'local_agent': {'reporting_host': 'jaeger'},
            'logging': True,
        },
        service_name=service_name,
    )
    return config.initialize_tracer()

tracer = init_tracer()
flask_tracer = FlaskTracing(tracer, True, app)

# Routes
@app.route('/')
@REQUEST_LATENCY.time()
def home():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    logging.info("Home route accessed")
    return "Welcome to Observability App!"

@app.route('/slow')
@REQUEST_LATENCY.time()
def slow():
    REQUEST_COUNT.labels(method='GET', endpoint='/slow').inc()
    logging.warning("Slow route accessed")
    time.sleep(2)
    return "This response was intentionally slow"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
