# ADR 002: Database-Per-Service Pattern

## Status
**Accepted** (Architecture Review Board Consensus, August 2026)

## Context & Problem Statement
To prevent tight coupling at the database tier and eliminate cross-service table joins, each microservice possesses its own isolated relational store (PostgreSQL instance).

## Decision Drivers
- High availability (99.99% target SLA)
- Sub-50ms P95 latency across API Gateway
- Data consistency across distributed multi-database topology
- Zero-trust compliance and regulatory auditability

## Considered Options
1. Monolithic single-database architecture
2. Distributed microservices with synchronous RPC only
3. Event-driven microservices architecture with Saga orchestration (Chosen)

## Decision Outcome
Adopted unanimously across the engineering organization.

### Positive Consequences
- True autonomous deployments across independent engineering teams.
- Fault isolation: A failure in Notification Service does not block Order checkout.
- Elastic autoscaling tailored to individual microservice workloads (e.g. Catalog scales higher on Black Friday).

### Negative Consequences
- Eventual consistency requires compensation logic and idempotency handling.
- Operational burden of managing Kafka clusters, Redis instances, and 10 separate relational schemas.

## Validation & Compliance
- Automated architecture compliance tests in `tests/e2e/`.
- Chaos engineering drills simulating network partitions and database node crashes.
