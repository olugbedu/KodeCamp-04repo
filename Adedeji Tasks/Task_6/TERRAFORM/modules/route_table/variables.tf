variable "vpc_id" {
  description = "The VPC ID"
  type        = string
}

variable "igw_id" {
  description = "The Internet Gateway ID"
  type        = string
}

variable "public_subnet_id" {
  description = "The public subnet ID"
  type        = string
}

variable "private_subnet_id" {
  description = "The private subnet ID"
  type        = string
}
