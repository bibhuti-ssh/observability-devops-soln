from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)

# Set up tracing
trace.set_tracer_provider(TracerProvider())
otlp_exporter = OTLPSpanExporter(endpoint="otlp-collector:4317")
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Instrument Flask
FlaskInstrumentor().instrument_app(app)

@app.route("/api/endpoint")
def api_endpoint():
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("api_endpoint"):
        # Your endpoint logic here
        return {"status": "success"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)