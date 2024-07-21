# Task 6 - Infrastructure as Code (Terraform)

## A detailed report with screenshots of each step.
This is a breakdown of the steps I took to set up a Virtual Private Cloud (VPC) with both public and private subnets. Implement routing, security groups, and network access control lists (NACLs) to ensure proper communication and security within the VPC, using TERRAFORM.

### Breakdown
#### AWS configure
- I started by configuring aws cli from my VSCODE terminal
![aws configure](images/aws_configure.png)

### **modules/scripts for ec2, vpc, subnet, nat_gateway, route_table, security_group.**

#### Ec2 module:  ![ec2 module](./TERRAFORM/modules/ec2/main.tf) 
I used a `Terraform data block` to attach a keypair already on my console to the instances, `Terraform resource block` to create the instances (public and private), `user_data` to set the path for the ngix installation ![user_data](images/user_data.png) 
![user_data](images/user_data2.png)
![ec2 instance](images/ec2_instance.png)

#### VPC module: ![vpc module](./TERRAFORM/modules/vpc/main.tf)
I created a vpc module including the internet gateway configuration using the `Terraform resource block`
![vpc](images/VPC.png)

#### Subnets module: ![subnet module](./TERRAFORM/modules/subnet/main.tf)
I created public and private subnets using the `Terraform resource block`

![subnets](images/subnets.png)

#### NAT Gateway module: ![nat_gateway module](./TERRAFORM/modules/nat_gateway/main.tf)
I created a NAT Gateway in the public subnet and allocated an Elastic IP for the NAT Gateway, using `Terraform resource block`.

![NAT gateway](images/nat.png)


#### Route Tables module: ![route_table module](./TERRAFORM/modules/route_table/main.tf)
I configured the public route table, associated it with public subnet and added the route to internet(IGW 0.0.0.0/0). Then, I configured the private route table, associated it with private subnet and addded nat gateway to ensure no direct route to internet(NAT 0.0.0.0/0).

![Route table](images/RT.png)


#### Security Groups module: ![security_group module](./TERRAFORM/modules/security_group/main.tf)
Using `Terraform resource block`  I created a Security Group for public instances, I named it PublicSecurityGroup and allowed the following protocols;
- Inbound HTTP (port 80) 
- HTTPS (port 443) traffic from anywhere (0.0.0.0/0).
- Inbound SSH (port 22) traffic from my local IP 
- All outbound traffic.
Then i created a Security Group for private instances, I named it PrivateSecurityGroup and allowed the following protocols;
- Inbound traffic from the PublicSubnet on required ports (MySQL port 3306).
- All outbound traffic.

![Security Group](images/security_groups.png)


#### Resource Map:

![resource map](images/Resource_map.png)


#### Terraform Appply:
![terraform apply](images/terraform_apply.png) 

#### Terraform Destroy:
![terraform destroy](images/terraform_destroy.png)

## Output of terraform plan:  ![plan](./TERRAFORM/tfplan.json)

## Summary - These components all work together to create a secure, efficient, and scalable network environment on AWS using Terraform(Infrasttucture as Code).