# Operations Runbook: Incident Response & Triage

## 1. Severity Definitions
- **SEV-1 (Critical)**: Total system outage, API Gateway unresponsive, or checkout flow degraded > 5%.
- **SEV-2 (High)**: Individual microservice offline, degraded performance (P99 > 2.0s), or Kafka consumer lag > 10,000.
- **SEV-3 (Moderate)**: Non-critical functionality degraded (e.g., analytics delay or slow email dispatch).

## 2. Immediate Triage Checklist
1. Check API Gateway status via Prometheus `/metrics` and Grafana overview dashboard.
2. Inspect Kubernetes pod status: `kubectl get pods -n cloudmart`.
3. Check Kafka consumer group lag: `kafka-consumer-groups.sh --bootstrap-server kafka:9092 --describe --group cloudmart-order`.
4. Check PostgreSQL connection saturation across per-service instances.
5. If Circuit Breaker is persistently OPEN, verify downstream network connectivity and database response time.

## 3. Escalation Contacts
- Incident Commander: `oncall-lead@cloudmart.internal`
- Platform Engineering: `platform-pager@cloudmart.internal`
