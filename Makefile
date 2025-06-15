IMAGE_NAME=fin_data_project_001
CONTAINER_NAME=fin_data_project_001_container

.PHONY: build run shell stop logs jaeger
.PHONY: venv install lint format

# 🐳 Build Docker image
build:
	docker build -t $(IMAGE_NAME) .

# 🚀 Run Docker container (main pipeline)
run:
	docker run --rm -it --name $(CONTAINER_NAME) -p 8000:8000 -v $(PWD):/app $(IMAGE_NAME)

# 🔄 Build and run in one step
build-run: build run

# 🐚 Open a shell in the Docker container
shell:
	docker run --rm -it --name $(CONTAINER_NAME) -p 8000:8000 -v $(PWD):/app $(IMAGE_NAME) /bin/bash

# 🛑 Stop the running Docker container
stop:
	-docker stop $(CONTAINER_NAME)

# 📜 Show Docker container logs
logs:
	docker logs $(CONTAINER_NAME)

# 🟣 Run Jaeger for OpenTelemetry tracing (optional)
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

# 📈 Prometheus metrics are available at http://localhost:8000/metrics when the container is running.

# 🐍 Create a Python virtual environment
venv:
	python3 -m venv .venv

# 📦 Install all Python dependencies in the virtual environment
install: venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements-core.txt -r requirements-llm.txt

# 🧹 Lint code with flake8
lint:
	. .venv/bin/activate && flake8 src/

# 🎨 Format code with black and isort
format:
	. .venv/bin/activate && black src/ && isort src/

# 📓 Launch Jupyter Notebook in the virtual environment
notebook:
	@if [ ! -d ".venv" ]; then \
		echo "Virtual environment not found. Run 'make install' first."; \
		exit 1; \
	fi
	. .venv/bin/activate && jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --no-browser

# 🧐 Type check with mypy
typecheck:
	. .venv/bin/activate && mypy src/

# 🧪 Run all tests with pytest and show coverage
test:
	. .venv/bin/activate && pytest --cov=src

# 🛫 Initialize Airflow DB and create admin user
airflow-init:
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && airflow db migrate && airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com || true

# 🌐 Start Airflow webserver (foreground, for VSCode terminal)
airflow-webserver:
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && airflow webserver --port 8080

# ⚙️ Start Airflow scheduler (foreground, for VSCode terminal)
airflow-scheduler:
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && airflow scheduler

# 🖥️ (Background) Start both Airflow webserver and scheduler in current terminal
airflow-up:
	@echo "Starting Airflow webserver and scheduler in the current terminal... 🚦"
	@echo "To stop them, press Ctrl+C or run 'make airflow-down'."
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && \
	nohup airflow webserver --port 8080 > airflow-webserver.log 2>&1 & \
	nohup airflow scheduler > airflow-scheduler.log 2>&1 & \
	sleep 2 && echo "Airflow webserver running on http://localhost:8080"

# 🛑 Stop Airflow webserver and scheduler background processes
airflow-down:
	@echo "Stopping Airflow webserver and scheduler... 🛑"
	-@pkill -f "airflow webserver"
	-@pkill -f "airflow scheduler"
	@echo "Stopped Airflow processes."

# 🖥️ (VSCode-friendly) Run Airflow webserver in foreground terminal
airflow-webserver-foreground:
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && airflow webserver --port 8080

# 🖥️ (VSCode-friendly) Run Airflow scheduler in foreground terminal
airflow-scheduler-foreground:
	. .venv/bin/activate && export AIRFLOW_HOME=$(PWD)/airflow && airflow scheduler