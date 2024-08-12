Objective
Set up a CI/CD pipeline with GitHub Actions to deploy a code (could be the code from your previous task) from GitHub to a Minikube cluster running on an EC2 instance deployed using Terraform.

Deliverables

Documentations of your processes

Screenshots of your results from each step

Application for Deployment

Docker image

Terraform Modules 

Kubernetes Manifests

 

Steps
Step 1: Prepare the Code Repository
Create a Repository on GitHub:
Create a new repository on GitHub and push your application code.
Add Your Application Code:
Add your application code to the repository.
Ensure you have a Dockerfile for your application to containerize it
Push image to Docker image registry
Create Kubernetes Manifests:
Add the necessary Kubernetes manifests (e.g., deployment.yaml, service.yaml) to a k8s directory in your repository.
Step 2: Set Up GitHub Actions
Create a GitHub Actions Workflow:
In your repository, create a .github/workflows directory.
Create a YAML file (e.g., deploy.yml) inside this directory with the required configurations.
Step 3: Set Up Terraform for EC2 and Minikube
Create Terraform Module:
Create terraform modules for your EC2, VPC, and any other resources you would like to use (taking considerations of the cost)
Initialize and Apply Terraform Configuration:
Create root modules 
Run the appropriate Terraform commands in your terminal to create an EC2 instance with Minikube running on it.
Step 4: Access the Minikube Cluster
SSH into EC2 Instance:
SSH into the created EC2 instance using the public IP output from Terraform.
Configure kubectl:
Inside the EC2 instance, configure kubectl to use the Minikube cluster.
Step 5: Automate Deployment with GitHub Actions
Update GitHub Actions Workflow:
Update the GitHub Actions workflow to deploy to the Minikube cluster on the EC2 instance. Ensure the Minikube instance's IP and SSH keys are securely managed.
 

Links
1.

GitHub Repo
Resources
https://docs.github.com/en/actions
https://minikube.sigs.k8s.io/docs/
https://registry.terraform.io/providers/hashicorp/aws/latest/docs.