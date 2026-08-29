# CloudMart: Enterprise Distributed Microservices Platform

[![CI/CD Pipeline](https://github.com/jani140992-hub/micro-services/actions/workflows/ci.yml/badge.svg)](https://github.com/jani140992-hub/micro-services)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Architecture](https://img.shields.io/badge/architecture-Microservices%20DDD-green.svg)](#architecture)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

CloudMart is a production-grade, distributed, cloud-native e-commerce and logistics microservices platform designed using **Domain-Driven Design (DDD)**, **Clean / Hexagonal Architecture**, **Event-Driven Choreography and Orchestration (Saga Pattern)**, and **CQRS / Outbox Pattern** for ultra-resilient distributed operations.

---

## Architectural Topology

```
                                     [ Web / Mobile Clients ]
                                                │
                                                ▼
                        ┌───────────────────────────────────────────────┐
                        │              API Gateway Service              │
                        │   Port: 8000 | Rate Limit, JWT, Route Proxy  │
                        └───────────────────────┬───────────────────────┘
                                                │
         ┌───────────────────┬──────────────────┼───────────────────┬───────────────────┐
         ▼                   ▼                  ▼                   ▼                   ▼
  ┌───────────────┐   ┌───────────────┐  ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
  │   Identity    │   │     User      │  │    Catalog    │   │   Inventory   │   │     Order     │
  │    Service    │   │    Service    │  │    Service    │   │    Service    │   │    Service    │
  │  Port: 8001   │   │  Port: 8002   │  │  Port: 8003   │   │  Port: 8004   │   │  Port: 8005   │
  └───────┬───────┘   └───────┬───────┘  └───────┬───────┘   └───────┬───────┘   └───────┬───────┘
          │                   │                  │                   │                   │
          └───────────────────┴───────────┬──────┴───────────────────┴───────────────────┘
                                          │
                        ┌─────────────────▼─────────────────┐
                        │    Apache Kafka / RabbitMQ Bus    │
                        │    (CloudEvents v1.0 Standard)    │
                        └─────────────────┬─────────────────┘
                                          │
         ┌───────────────────┬────────────┴─────┬───────────────────┬───────────────────┐
         ▼                   ▼                  ▼                   ▼                   ▼
  ┌───────────────┐   ┌───────────────┐  ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
  │    Payment    │   │   Shipping    │  │ Notification  │   │   Analytics   │   │ Prometheus /  │
  │    Service    │   │    Service    │  │    Service    │   │    Service    │   │    Grafana    │
  │  Port: 8006   │   │  Port: 8007   │  │  Port: 8008   │   │  Port: 8009   │   │  Port: 9090   │
  └───────────────┘   └───────────────┘  └───────────────┘   └───────────────┘   └───────────────┘
```

---

## Core Microservices Roster

| Microservice | Port | Database | Primary Responsibility | Architectural Patterns |
| :--- | :--- | :--- | :--- | :--- |
| **API Gateway** | `8000` | In-Memory / Redis | Edge routing, JWT validation, Leaky Bucket rate limiter, Circuit Breaking | Reverse Proxy, API Composition |
| **Identity Service** | `8001` | PostgreSQL (`auth_db`) | User authentication, Argon2id hashing, JWT access/refresh token rotation, RBAC | OAuth2 / OIDC, Token Blacklist |
| **User Profile Service** | `8002` | PostgreSQL (`user_db`) | Customer profiles, address book, KYC compliance, GDPR data export & purge | CQRS, Soft Deletion, Audit Logging |
| **Catalog Service** | `8003` | PostgreSQL (`catalog_db`) | Taxonomy, product variants, dynamic pricing, faceted attribute search | CQRS, Read Model Caching |
| **Inventory Service** | `8004` | PostgreSQL (`inventory_db`)| Multi-warehouse stock tracking, 15-min reservation hold with TTL, restocking | Pessimistic Locking, TTL Reservations |
| **Order Service** | `8005` | PostgreSQL (`order_db`) | Order lifecycle management, Saga Orchestration, Payment & Stock coordination | Saga Orchestrator, Transactional Outbox |
| **Payment Service** | `8006` | PostgreSQL (`payment_db`) | Payment intents, Stripe/PayPal mock adapters, Double-entry financial ledger | Idempotency Key, Financial Ledger |
| **Shipping Service** | `8007` | PostgreSQL (`shipping_db`) | Carrier selection (FedEx/UPS/DHL mock), dispatching, tracking milestone updates| State Machine, Geo-Routing |
| **Notification Service** | `8008` | PostgreSQL (`notify_db`) | Multi-channel dispatch (Email, SMS, Webhook, WebSocket), Jinja templating | DLQ Retry, Event-Driven Consumer |
| **Analytics Service** | `8009` | PostgreSQL / Redis | Real-time streaming metrics, revenue analytics, cart abandonment, Prometheus | Stream Ingestion, Sliding Window Aggregation |

---

## Shared Kernel Library (`shared/`)

Each microservice leverages a centralized, versioned shared library providing:
1. **CloudEvents Event Bus**: Standardized event serialization, schema validation, idempotency detection, and Kafka/RabbitMQ adapters.
2. **Distributed Tracing & Telemetry**: OpenTelemetry correlation IDs (`X-Correlation-ID`, `X-Trace-ID`), structured JSON logging, and Prometheus latency collectors.
3. **Resilience Engineering**: Circuit breaker state machine (Closed -> Open -> Half-Open), exponential backoff jittered retry, and bulkhead thread pool isolation.
4. **Security & Cryptography**: Ed25519 / RSA-256 JWT validation, fine-grained RBAC permission evaluation, and field-level encryption for PII.
5. **Database Abstraction**: Async SQLAlchemy session management, generic repository interfaces, Unit of Work pattern, and audit trail mixins.
6. **Protobuf & gRPC Contracts**: High-throughput inter-service synchronous communication specifications.

---

## Infrastructure as Code & Orchestration

- **Docker Compose**: Complete development stack orchestration with per-service isolated databases, Kafka, Redis, and observability.
- **Kubernetes (K8s)**: Production-ready manifests with Deployments, ClusterIP Services, Ingress, Horizontal Pod Autoscalers (HPA), and ConfigMaps.
- **Helm Charts**: Enterprise Helm packaging (`helm/cloudmart`) for parameterized multi-environment deployments (dev, staging, prod).
- **Observability**: Pre-configured Prometheus alerting rules (`alerts.yml`) and Grafana analytics dashboard.

---

## Quickstart Guide

### Prerequisites
- Python 3.12+
- Docker & Docker Compose
- Make (optional, but recommended)

### 1. Clone & Setup
```bash
git clone git@github.com:jani140992-hub/micro-services.git
cd micro-services
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

### 2. Launch Entire Distributed Mesh
```bash
docker-compose up -d
```

### 3. Verify Health
```bash
curl http://localhost:8000/health
```

### 4. Run Automated Test Suites
```bash
pytest tests/
```

---

## License
Distributed under the MIT License. See `LICENSE` for more information.
