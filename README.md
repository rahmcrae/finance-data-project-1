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

## ⚡ CI/CD

- 🛡️ GitHub Actions workflow runs linting and tests on every push and PR.

---