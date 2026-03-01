from flask import Flask
import time
import random
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(endpoint="otel-collector:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "backend_requests_total",
    "Total backend requests"
)

ERROR_COUNT = Counter(
    "backend_errors_total",
    "Total backend errors"
)

REQUEST_LATENCY = Histogram(
    "backend_request_duration_seconds",
    "Backend request latency"
)

@app.route("/")
def hello():
    REQUEST_COUNT.inc()

    with REQUEST_LATENCY.time():
        with tracer.start_as_current_span("backend-work"):

            if random.random() < 0.05:
                ERROR_COUNT.inc()
                return "Internal Error", 500

            time.sleep(0.2)
            return "Hello from backend!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
