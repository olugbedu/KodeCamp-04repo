variable "aws_region" {
  description = "The AWS region to deploy in"
  type        = string
  default     = "eu-west-1"
}

variable "key_name" {
  description = "The name of the key pair to use for SSH access"
  type        = string
}
