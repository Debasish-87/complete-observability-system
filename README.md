# Complete Observability System (Metrics, Logs & Traces)

## Objective

Build a complete containerized observability system that includes:

* Metrics collection using Prometheus
* Centralized log aggregation using Loki
* Distributed tracing using Jaeger
* Unified visualization via Grafana dashboards

## Tech Stack

* Python (Flask)
* Docker & Docker Compose
* Prometheus (Metrics)
* Loki + Promtail (Logs)
* Jaeger (Tracing)
* Grafana (Visualization)

---

## Project Structure

```
.
├── app/                            # Flask app with logs and tracing
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── prometheus/prometheus.yml       # Prometheus config
├── promtail/promtail-config.yml    # Promtail config
├── docker-compose.yml              # Docker Compose stack
├── Complete Observability System-1750458231469.json  # Grafana dashboard JSON
```

---

## How to Run

1. Clone the repository:

```bash
git clone <repo-url>
cd complete-observability
```

2. Start the stack:

```bash
docker compose up --build
```

3. Access the following dashboards:

| Tool       | URL                                              |
| ---------- | ------------------------------------------------ |
| Flask App  | [http://localhost:5000](http://localhost:5000)   |
| Prometheus | [http://localhost:9090](http://localhost:9090)   |
| Jaeger UI  | [http://localhost:16686](http://localhost:16686) |
| Grafana    | [http://localhost:3000](http://localhost:3000)   |

Grafana default credentials:

* **Username:** admin
* **Password:** admin

---

## Deliverables

* `docker-compose.yml`
* Prometheus and Promtail configuration files
* Flask app instrumented with metrics, logs, and tracing
* Grafana dashboard JSON file
* Log samples and trace visualizations
* Screenshot evidence (see below)

---

## Screenshots

### 1. Flask App Running

![Flask App Welcome](./screenshots/1-flask-app.png)

---

### 2. Prometheus Dashboard

![Prometheus UI](./screenshots/2-prometheus.png)

---

### 3. Jaeger UI Traces

![Jaeger Tracing](./screenshots/3-jaeger.png)

---

### 4. Grafana Observability Dashboard

![Grafana Dashboard](./screenshots/4-grafana.png)

---

## Summary

This project demonstrates a production-style observability system built with open-source tools in a Docker-based environment. It showcases real-time metrics collection, centralized logging, and distributed tracing for a sample application, all visualized through Grafana.
