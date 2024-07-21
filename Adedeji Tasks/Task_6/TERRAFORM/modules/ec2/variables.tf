variable "ami" {
  description = "The AMI ID"
  type        = string
}

variable "instance_type" {
  description = "The instance type"
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

variable "public_sg_id" {
  description = "The public security group ID"
  type        = string
}

variable "private_sg_id" {
  description = "The private security group ID"
  type        = string
}

variable "key_name" {
  description = "MyFirstKeyPair.pem"
  type        = string
}
