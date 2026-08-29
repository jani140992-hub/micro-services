# PostgreSQL RDS Instances for Microservices (Database-per-Service)
resource "aws_db_subnet_group" "cloudmart" {
  name       = "cloudmart-db-subnet-group"
  subnet_ids = module.vpc.private_subnets
}

resource "aws_db_instance" "db_identity_service" {
  identifier             = "cloudmart-identity-service-db"
  engine                 = "postgres"
  engine_version         = "16.2"
  instance_class         = "db.m6i.large"
  allocated_storage      = 50
  max_allocated_storage  = 500
  db_name                = "identity_service_db"
  username               = "cloudmart_admin"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.cloudmart.name
  skip_final_snapshot    = false
  multi_az               = true
  backup_retention_period = 30
  deletion_protection    = true
}

resource "aws_db_instance" "db_user_service" {
  identifier             = "cloudmart-user-service-db"
  engine                 = "postgres"
  engine_version         = "16.2"
  instance_class         = "db.m6i.large"
  allocated_storage      = 50
  max_allocated_storage  = 500
  db_name                = "user_service_db"
  username               = "cloudmart_admin"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.cloudmart.name
  skip_final_snapshot    = false
  multi_az               = true
  backup_retention_period = 30
  deletion_protection    = true
}

resource "aws_db_instance" "db_catalog_service" {
  identifier             = "cloudmart-catalog-service-db"
  engine                 = "postgres"
  engine_version         = "16.2"
  instance_class         = "db.m6i.large"
  allocated_storage      = 50
  max_allocated_storage  = 500
  db_name                = "catalog_service_db"
  username               = "cloudmart_admin"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.cloudmart.name
  skip_final_snapshot    = false
  multi_az               = true
  backup_retention_period = 30
  deletion_protection    = true
}

resource "aws_db_instance" "db_inventory_service" {
  identifier             = "cloudmart-inventory-service-db"
  engine                 = "postgres"
  engine_version         = "16.2"
  instance_class         = "db.m6i.large"
  allocated_storage      = 50
  max_allocated_storage  = 500
  db_name                = "inventory_service_db"
  username               = "cloudmart_admin"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.cloudmart.name
  skip_final_snapshot    = false
  multi_az               = true
  backup_retention_period = 30
  deletion_protection    = true
}

resource "aws_db_instance" "db_order_service" {
  identifier             = "cloudmart-order-service-db"
  engine                 = "postgres"
  engine_version         = "16.2"
  instance_class         = "db.m6i.large"
  allocated_storage      = 50
  max_allocated_storage  = 500
  db_name                = "order_service_db"
  username               = "cloudmart_admin"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.cloudmart.name
  skip_final_snapshot    = false
  multi_az               = true
  backup_retention_period = 30
  deletion_protection    = true
}

resource "aws_db_instance" "db_payment_service" {
  identifier             = "cloudmart-payment-service-db"
  engine                 = "postgres"
  engine_version         = "16.2"
  instance_class         = "db.m6i.large"
  allocated_storage      = 50
  max_allocated_storage  = 500
  db_name                = "payment_service_db"
  username               = "cloudmart_admin"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.cloudmart.name
  skip_final_snapshot    = false
  multi_az               = true
  backup_retention_period = 30
  deletion_protection    = true
}

resource "aws_db_instance" "db_shipping_service" {
  identifier             = "cloudmart-shipping-service-db"
  engine                 = "postgres"
  engine_version         = "16.2"
  instance_class         = "db.m6i.large"
  allocated_storage      = 50
  max_allocated_storage  = 500
  db_name                = "shipping_service_db"
  username               = "cloudmart_admin"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.cloudmart.name
  skip_final_snapshot    = false
  multi_az               = true
  backup_retention_period = 30
  deletion_protection    = true
}

resource "aws_db_instance" "db_notification_service" {
  identifier             = "cloudmart-notification-service-db"
  engine                 = "postgres"
  engine_version         = "16.2"
  instance_class         = "db.m6i.large"
  allocated_storage      = 50
  max_allocated_storage  = 500
  db_name                = "notification_service_db"
  username               = "cloudmart_admin"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.cloudmart.name
  skip_final_snapshot    = false
  multi_az               = true
  backup_retention_period = 30
  deletion_protection    = true
}

resource "aws_db_instance" "db_analytics_service" {
  identifier             = "cloudmart-analytics-service-db"
  engine                 = "postgres"
  engine_version         = "16.2"
  instance_class         = "db.m6i.large"
  allocated_storage      = 50
  max_allocated_storage  = 500
  db_name                = "analytics_service_db"
  username               = "cloudmart_admin"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.cloudmart.name
  skip_final_snapshot    = false
  multi_az               = true
  backup_retention_period = 30
  deletion_protection    = true
}
