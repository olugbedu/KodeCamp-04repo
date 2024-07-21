variable "vpc_id" {
  description = "The VPC ID"
  type        = string
}

variable "public_subnet_cidr" {
  description = "The CIDR block for the public subnet"
  type        = string
}

variable "my_ip" {
  description = "Your local IP address"
  type        = string
}
