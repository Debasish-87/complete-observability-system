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

![83921eb3-31fd-47f6-8571-0123424f7653](https://github.com/user-attachments/assets/e1b3ce5e-c5b0-4488-9df0-bf49cc7da33d)

---

### 2. Prometheus Dashboard

![928c675d-4882-4f81-b828-0b86e62f0554](https://github.com/user-attachments/assets/8dc25792-07e5-4999-afb6-55a36e469da6)

---

### 3. Jaeger UI Traces

![1b18dac2-adf0-437c-afc1-2025b0bbd919](https://github.com/user-attachments/assets/f451a666-3527-4200-a7d4-08a66cfcbba5)

---

### 4. Grafana Observability Dashboard

![e3ee7173-e144-42ca-a07d-0f6451b9c9da](https://github.com/user-attachments/assets/356178fa-76e5-48fa-b446-cd234d293f96)

---

## Summary

This project demonstrates a production-style observability system built with open-source tools in a Docker-based environment. It showcases real-time metrics collection, centralized logging, and distributed tracing for a sample application, all visualized through Grafana.
