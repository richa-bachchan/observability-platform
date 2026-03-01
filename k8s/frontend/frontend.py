from flask import Flask
import requests
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(endpoint="otel-collector:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

RequestsInstrumentor().instrument()

app = Flask(__name__)

@app.route("/")
def call_backend():
    with tracer.start_as_current_span("frontend-work"):
        response = requests.get("http://backend:5000")
        return "Frontend received: " + response.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
