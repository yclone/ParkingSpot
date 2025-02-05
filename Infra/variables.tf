variable "project_name" {
  description = "Nome do projeto"
  default     = "tr-ai"
}

variable "aws_region" {
  description = "Região AWS"
  default     = "us-east-1"
}

variable "environment" {
  description = "Ambiente (dev, prod, etc)"
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR da VPC"
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "AZs a serem utilizadas"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

variable "private_subnet_cidrs" {
  description = "CIDRs das subnets privadas"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "public_subnet_cidrs" {
  description = "CIDRs das subnets públicas"
  type        = list(string)
  default     = ["10.0.101.0/24", "10.0.102.0/24"]
}

variable "common_tags" {
  description = "Tags comuns para todos os recursos"
  type        = map(string)
  default = {
    Project     = "tr-ai"
    Environment = "dev"
    Terraform   = "true"
  }
}
