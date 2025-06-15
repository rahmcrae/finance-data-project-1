from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

# from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
# Example: To export to Jaeger, you could use:
# from opentelemetry.exporter.jaeger.thrift import JaegerExporter
# from opentelemetry.sdk.trace.export import BatchSpanProcessor

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Remove or comment out ConsoleSpanExporter to silence console logs
# span_processor = BatchSpanProcessor(ConsoleSpanExporter())
# trace.get_tracer_provider().add_span_processor(span_processor)

# Example Jaeger exporter setup (uncomment and configure if needed)
# from opentelemetry.exporter.jaeger.thrift import JaegerExporter
# from opentelemetry.sdk.trace.export import BatchSpanProcessor
# jaeger_exporter = JaegerExporter(
#     agent_host_name="localhost",
#     agent_port=6831,
# )
# span_processor = BatchSpanProcessor(jaeger_exporter)
# trace.get_tracer_provider().add_span_processor(span_processor)


def traced(func):
    def wrapper(*args, **kwargs):
        with tracer.start_as_current_span(func.__name__):
            return func(*args, **kwargs)

    return wrapper


@traced
def summarize_timeseries(df, asset_name):
    trend = "increasing" if df.iloc[-1] > df.iloc[0] else "decreasing"
    summary = f"Asset {asset_name} shows a {trend} trend in {len(df)} data points."
    return summary


# Placeholder for LLM integration (e.g., OpenAI, Anthropic, etc.)
# def summarize_timeseries_with_llm(df, asset_name):
#     # Use LLM API to generate a summary
#     pass
