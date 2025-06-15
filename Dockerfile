# --- Stage 1: Build base with core dependencies ---
FROM python:3.10-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential gcc git curl && \
    rm -rf /var/lib/apt/lists/*

# Install only core project libraries first (for better caching)
COPY requirements-core.txt .
RUN pip install --no-cache-dir "pip<24.1" && \
    pip install --no-cache-dir -r requirements-core.txt

# --- Stage 2: Add LLM/AI dependencies ---
FROM base AS ai

COPY requirements-llm.txt .
RUN pip install --no-cache-dir -r requirements-llm.txt

# --- Stage 3: Final image with all code ---
FROM ai

WORKDIR /app

# Set PYTHONPATH so 'src' is importable
ENV PYTHONPATH=/app

COPY . .

CMD ["python", "src/ingestion/pipeline_runner.py"]