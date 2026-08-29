output "vpc_id" {
  value = module.vpc.vpc_id
}

output "eks_cluster_endpoint" {
  value = module.eks.cluster_endpoint
}

output "kafka_bootstrap_brokers_tls" {
  value = aws_msk_cluster.cloudmart_kafka.bootstrap_brokers_tls
}

output "redis_primary_endpoint" {
  value = aws_elasticache_replication_group.cloudmart_redis.primary_endpoint_address
}
