resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
  tags = {
    Name = "KCVPC"
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "KCVPC-IGW"
  }
}
