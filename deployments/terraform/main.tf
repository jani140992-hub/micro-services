terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.40"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.26"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.12"
    }
  }
  backend "s3" {
    bucket         = "cloudmart-terraform-state-prod"
    key            = "mesh/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "cloudmart-tf-locks"
  }
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Environment = var.environment
      Project     = "CloudMart Distributed Platform"
      ManagedBy   = "Terraform"
    }
  }
}

# VPC and Subnets
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
  name    = "cloudmart-vpc"
  cidr    = var.vpc_cidr
  azs     = ["${var.aws_region}a", "${var.aws_region}b", "${var.aws_region}c"]
  private_subnets = var.private_subnet_cidrs
  public_subnets  = var.public_subnet_cidrs
  enable_nat_gateway = true
  single_nat_gateway = false
  enable_dns_hostnames = true
}

# AWS EKS Cluster
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"
  cluster_name    = "cloudmart-eks-cluster"
  cluster_version = "1.29"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnets
  cluster_endpoint_public_access = true
  eks_managed_node_groups = {
    default = {
      min_size     = 3
      max_size     = 12
      desired_size = 6
      instance_types = ["m6i.xlarge", "m5.xlarge"]
    }
  }
}
