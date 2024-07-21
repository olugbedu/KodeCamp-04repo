variable "vpc_id" {
  description = "The VPC ID"
  type        = string
}

variable "public_subnet_cidr" {
  description = "The CIDR block for the public subnet"
  type        = string
}

variable "private_subnet_cidr" {
  description = "The CIDR block for the private subnet"
  type        = string
}

variable "public_subnet_az" {
  description = "The availability zone for the public subnet"
  type        = string
}

variable "private_subnet_az" {
  description = "The availability zone for the private subnet"
  type        = string
}
