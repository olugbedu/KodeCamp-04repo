Objective:
1. Using Terraform, design and set up a Virtual Private Cloud (VPC) with both public and private subnets. Implement routing, security groups, and network access control lists (NACLs) to ensure proper communication and security within the VPC and an Ubuntu EC2 instance in each subnet. Work in the AWS EU-West-1 (Ireland) region.
2. Create separate child modules for your resources and reference them in your root module for readability and re-usability of your code.
3. Write a script to install Nginx on your EC2 instance in the public subnet on deployment
4. Write a script to install PostgreSQL on your EC2 instance in the public subnet on deployment
5. Clean up resource on completion using terraform destroy
 
Requirements:
Create a VPC:
Name: KCVPC
IPv4 CIDR block: 10.0.0.0/16
Create Subnets:
Public Subnet:
Name: PublicSubnet
IPv4 CIDR block: 10.0.1.0/24
Availability Zone: Select any one from your region
Private Subnet:
Name: PrivateSubnet
IPv4 CIDR block: 10.0.2.0/24
Availability Zone: Select any one from your region (preferably the same as the Public Subnet for simplicity)
Configure an Internet Gateway (IGW):
Create and attach an IGW to KCVPC.
Configure Route Tables:
Public Route Table:
Name: PublicRouteTable
Associate PublicSubnet with this route table.
Add a route to the IGW (0.0.0.0/0 -> IGW).
Private Route Table:
Name: PrivateRouteTable
Associate PrivateSubnet with this route table.
Ensure no direct route to the internet.
Configure NAT Gateway:
Create a NAT Gateway in the PublicSubnet.
Allocate an Elastic IP for the NAT Gateway.
Update the PrivateRouteTable to route internet traffic (0.0.0.0/0) to the NAT Gateway.
Set Up Security Groups:
Create a Security Group for public instances (e.g., web servers):
Allow inbound HTTP (port 80) and HTTPS (port 443) traffic from anywhere (0.0.0.0/0).
Allow inbound SSH (port 22) traffic from a specific IP (e.g., your local IP). (https://www.whatismyip.com/)
Allow all outbound traffic.
Create a Security Group for private instances (e.g., database servers):
Allow inbound traffic from the PublicSubnet on required ports (e.g., PostgreSQL port).
Allow all outbound traffic.
Network ACLs:
Configure NACLs for additional security on both subnets.
Public Subnet NACL: Allow inbound HTTP, HTTPS, and SSH traffic. Allow outbound traffic.
Private Subnet NACL: Allow inbound traffic from the public subnet. Allow outbound traffic to the public subnet and internet.
Deploy Instances:
Launch an EC2 instance in the PublicSubnet:
Use the public security group.
Verify that the instance can be accessed via the internet.
Launch an EC2 instance in the PrivateSubnet:
Use the private security group.
Verify that the instance can access the internet through the NAT Gateway and can communicate with the public instance.
Deliverables:
1. A detailed report with screenshots of each step.
2. Output of terraform plan [terraform plan -out tfplan.json or terraform plan -out tfplan.txt]
Links
1.

Github Repo Link
Resources
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html
https://nginx.org/en/
https://www.postgresql.org/
https://www.youtube.com/watch?v=eEbstFkbl9w&ab_channel=AWSDevelopers