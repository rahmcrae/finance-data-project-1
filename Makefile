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

notebook:
	@if [ ! -d ".venv" ]; then \
		echo "Virtual environment not found. Run 'make install' first."; \
		exit 1; \
	fi
	. .venv/bin/activate && jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --no-browser

typecheck:
	. .venv/bin/activate && mypy src/

test:
	. .venv/bin/activate && pytest --cov=src

airflow-init:
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && airflow db migrate && airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com || true

airflow-webserver:
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && airflow webserver --port 8080

airflow-scheduler:
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && airflow scheduler

# VSCode-friendly: Run both Airflow processes in the current terminal (backgrounded)
airflow-up:
	@echo "Starting Airflow webserver and scheduler in the current terminal..."
	@echo "To stop them, press Ctrl+C or run 'make airflow-down'."
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && \
	nohup airflow webserver --port 8080 > airflow-webserver.log 2>&1 & \
	nohup airflow scheduler > airflow-scheduler.log 2>&1 & \
	sleep 2 && echo "Airflow webserver running on http://localhost:8080"

airflow-down:
	@echo "Stopping Airflow webserver and scheduler..."
	-@pkill -f "airflow webserver"
	-@pkill -f "airflow scheduler"
	@echo "Stopped Airflow processes."

# Simple: Run Airflow webserver and scheduler in two VSCode terminals
airflow-webserver-foreground:
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && airflow webserver --port 8080

airflow-scheduler-foreground:
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && airflow scheduler