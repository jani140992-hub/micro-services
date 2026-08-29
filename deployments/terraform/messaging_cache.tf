# Amazon MSK (Managed Kafka Cluster)
resource "aws_msk_cluster" "cloudmart_kafka" {
  cluster_name           = "cloudmart-kafka-prod"
  kafka_version          = "3.6.0"
  number_of_broker_nodes = 3

  broker_node_group_info {
    instance_type   = "kafka.m5.large"
    client_subnets  = module.vpc.private_subnets
    security_groups = [aws_security_group.kafka_sg.id]
    storage_info {
      ebs_storage_info {
        volume_size = 500
      }
    }
  }

  encryption_info {
    encryption_in_transit {
      client_broker = "TLS"
      in_cluster    = true
    }
  }
}

resource "aws_security_group" "kafka_sg" {
  name        = "cloudmart-kafka-security-group"
  vpc_id      = module.vpc.vpc_id
  description = "Security group for CloudMart MSK cluster"

  ingress {
    from_port   = 9092
    to_port     = 9098
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Redis Cluster
resource "aws_elasticache_replication_group" "cloudmart_redis" {
  replication_group_id          = "cloudmart-redis-cluster"
  description                   = "CloudMart High Availability Redis Cluster"
  node_type                     = "cache.r6g.large"
  num_cache_clusters            = 3
  port                          = 6379
  automatic_failover_enabled    = true
  multi_az_enabled              = true
  subnet_group_name             = aws_elasticache_subnet_group.redis_subnet_group.name
  security_group_ids            = [aws_security_group.redis_sg.id]
  at_rest_encryption_enabled    = true
  transit_encryption_enabled    = true
}

resource "aws_elasticache_subnet_group" "redis_subnet_group" {
  name       = "cloudmart-redis-subnets"
  subnet_ids = module.vpc.private_subnets
}

resource "aws_security_group" "redis_sg" {
  name        = "cloudmart-redis-sg"
  vpc_id      = module.vpc.vpc_id
  description = "Allow Redis traffic from microservices"

  ingress {
    from_port   = 6379
    to_port     = 6379
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }
}
