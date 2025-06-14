# Financial Engineering AI

A modular project for market data analysis, risk modeling, and AI-assisted insights.

## Telemetry & Monitoring Every Function Call

Yes, you can collect telemetry on every function in a Python application using decorators or tracing libraries. This is typically done with:

- **Custom decorators**: Wrap each function to log calls, arguments, execution time, etc.
- **OpenTelemetry**: Industry standard for distributed tracing and metrics, integrates with many backends (Prometheus, Jaeger, etc.).

### Example 1: Simple Logging Decorator

```python
from loguru import logger
import time

def telemetry(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        logger.info(f"{func.__name__} finished in {duration:.4f}s")
        return result
    return wrapper

@telemetry
def my_function(x):
    return x * 2
```

### Example 2: OpenTelemetry for Automatic Tracing

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

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
def my_function(x):
    return x * 2
```

### Example 3: Auto-Instrumentation

For frameworks (Flask, FastAPI, etc.), OpenTelemetry can auto-instrument all routes and handlers. For custom code, you can use decorators or metaprogramming to wrap all functions in a module/class.

**Summary:**  
- Use decorators for simple telemetry/logging.
- Use OpenTelemetry for robust, production-grade tracing and metrics.
- Export traces to a backend (Prometheus, Jaeger, etc.) for visualization and alerting.

## OpenTelemetry Integration

This project uses [OpenTelemetry](https://opentelemetry.io/) for tracing and metrics.  
Traces are exported to the console by default.  
To export to Prometheus, Jaeger, or another backend, replace `ConsoleSpanExporter()` with the appropriate exporter in your code.

## Agent-based Pipeline

- **Ingester Agent:** Fetches and stores raw financial data.
- **Analyzer Agent:** Loads, analyzes, and summarizes data (with LLM integration planned).

LLM-based summaries can be implemented using OpenAI or similar APIs in the future.

## Docker Build Performance Tips

- Ensure your `.dockerignore` excludes large files, datasets, and unnecessary directories.
- Place `COPY requirements.txt .` and `RUN pip install ...` before `COPY . .` to maximize Docker layer caching.
- Keep your `requirements.txt` as minimal as possible.
- Use a fast and stable internet connection.
- If you only need Jupyter or a subset of tools, consider splitting your requirements and using multi-stage builds.