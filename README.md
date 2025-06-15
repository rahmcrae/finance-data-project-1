# 💹 Financial Engineering AI

A modular project for market data analysis, risk modeling, and AI-assisted insights.

## ✨ Features

- 🏗️ Modular ingestion, feature engineering, and AI summarization
- 🤖 Agent-based pipeline (ingester, analyzer)
- 📊 Telemetry and monitoring with OpenTelemetry and Prometheus
- 📝 Robust logging with Loguru
- 📈 Visualization with Plotly and Altair
- 🧹 Linting, formatting, and type checking for code quality

## 🚀 Onboarding & Setup

### 1️⃣ Prerequisites

- 🐳 [Docker](https://www.docker.com/products/docker-desktop/) installed
- ⚙️ (Optional) [Make](https://www.gnu.org/software/make/) for easier commands

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/your-org/your-repo.git
cd your-repo/finance-data-project-1
```

### 3️⃣ Build the Docker Image

```sh
make build
```

### 4️⃣ Run the Project

```sh
make run
```

This will execute the main pipeline and print results to the console.

### 5️⃣ Open a Shell in the Container

```sh
make shell
```

You can use this to run Jupyter, Python, or other tools interactively.

### 6️⃣ Run Jupyter Notebook (Optional)

Inside the container shell:

```sh
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --no-browser
```

Then open [http://localhost:8888](http://localhost:8888) in your browser.

---

## 🩺 Monitoring & Telemetry

- **Prometheus Metrics:**  
  The pipeline exposes metrics at [http://localhost:8000/metrics](http://localhost:8000/metrics) when running.  
  You can use Prometheus or simply visit the URL to see live metrics.

- **Jaeger Tracing (Optional):**  
  To view traces, run Jaeger locally:
  ```sh
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
  ```
  Then open [http://localhost:16686](http://localhost:16686) in your browser.

---

## 🗂️ Project Structure

```
finance-data-project-1/
├── src/                # Source code (ingestion, features, ai, etc.)
├── scripts/            # Pipeline runner and utility scripts
├── notebooks/          # Jupyter notebooks for EDA and prototyping
├── requirements-core.txt
├── requirements-llm.txt
├── Dockerfile
├── Makefile
└── README.md
```

## 📡 Telemetry & Monitoring

- Uses OpenTelemetry for tracing.
- Prometheus client for metrics.
- Logs are handled by Loguru.

## 🧹 Linting, Formatting, and Testing

- 🔍 Lint: `flake8`
- 🎨 Format: `black`, `isort`
- 🧐 Type check: `mypy`
- 🧪 Test: `pytest`, `pytest-cov`

### ⚡ How to Fix Lint Errors

If you run `make lint` and still see line length errors (`E501`), but `make format` reports "files left unchanged," it means `black` is using a longer line length than `flake8`'s default (79).  
To resolve this, you can:

- **Option 1:** Configure `flake8` to allow longer lines (e.g., 88, which is `black`'s default):

Create a `.flake8` file in your project root with:

```
[flake8]
max-line-length = 88
```

- **Option 2:** Override the line length for `black` in `pyproject.toml`:

```toml
[tool.black]
line-length = 79
```

Then, re-run `make format` and `make lint`.

### ⚠️ Note on Formatting and Linting

If you keep seeing `E501 line too long` errors after running `black` and `isort`, it's because:
- `black` defaults to a line length of 88, but `flake8` may still enforce 79 or 88 depending on your `.flake8` config.
- If a line is longer than your `.flake8` `max-line-length`, you must manually break it up.

**How to fix:**
- Manually split any lines longer than your `.flake8` `max-line-length` (e.g., 88).
- Re-run `make lint` to confirm.

**If you want to avoid this in the future:**
- Always keep your `.flake8` `max-line-length` and `black`'s line length in sync.
- You can set `black`'s line length with:  
  `black --line-length 88 src/`

---

## ⚡ CI/CD

- 🛡️ GitHub Actions workflow runs linting and tests on every push and PR.

## 🐍 Local Development with Virtual Environment

To use a virtual environment for local development and code formatting:

```sh
make venv
make install
```

To auto-format and lint your code:

```sh
make format
make lint
```