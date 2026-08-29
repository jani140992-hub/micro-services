# Operations Runbook: Disaster Recovery & Failover

## 1. Recovery Objectives
- **RTO (Recovery Time Objective)**: < 15 minutes
- **RPO (Recovery Point Objective)**: < 1 minute

## 2. Multi-Region Failover Procedure
1. Verify primary region failure via external health checks.
2. Promote secondary AWS region RDS PostgreSQL read replicas to primary standalone instances.
3. Update Kubernetes ConfigMaps to point to newly promoted database endpoints.
4. Route 53 DNS switch: redirect `api.cloudmart.com` traffic to secondary region ingress controller.
5. Replay uncommitted transactional outbox messages from backup logs.
