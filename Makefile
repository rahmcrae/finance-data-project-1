IMAGE_NAME=fin_data_project_001
CONTAINER_NAME=fin_data_project_001_container

.PHONY: build run shell stop logs jaeger
.PHONY: venv install lint format

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -it --name $(CONTAINER_NAME) -p 8000:8000 -v $(PWD):/app $(IMAGE_NAME)

build-run: build run

shell:
	docker run --rm -it --name $(CONTAINER_NAME) -p 8000:8000 -v $(PWD):/app $(IMAGE_NAME) /bin/bash

stop:
	-docker stop $(CONTAINER_NAME)

logs:
	docker logs $(CONTAINER_NAME)

# Run Jaeger for OpenTelemetry tracing (optional)
jaeger:
	docker run -d --name jaeger \
		-e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
		-p 5775:5775/udp \
		-p 6831:6831/udp \
		-p 6832:6832/udp \
		-p 5778:5778 \
		-p 16686:16686 \
		-p 14268:14268 \
		-p 14250:14250 \
		-p 9411:9411 \
		jaegertracing/all-in-one:1.53

# Prometheus metrics are available at http://localhost:8000/metrics when the container is running.

venv:
	python3 -m venv .venv

install: venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements-core.txt -r requirements-llm.txt

lint:
	. .venv/bin/activate && flake8 src/

format:
	. .venv/bin/activate && black src/ && isort src/