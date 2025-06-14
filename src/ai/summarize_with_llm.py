from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

# Set up OpenTelemetry tracing (do this once in your app, ideally in your entrypoint)
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
span_processor = BatchSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

def traced(func):
    def wrapper(*args, **kwargs):
        with tracer.start_as_current_span(func.__name__):
            return func(*args, **kwargs)
    return wrapper

@traced
def summarize_timeseries(df, asset_name):
    trend = "increasing" if df.iloc[-1] > df.iloc[0] else "decreasing"
    summary = f"Asset {asset_name} shows a {trend} trend over the period with {len(df)} data points."
    return summary

# Placeholder for LLM integration (e.g., OpenAI, Anthropic, etc.)
# def summarize_timeseries_with_llm(df, asset_name):
#     # Use LLM API to generate a summary
#     pass
