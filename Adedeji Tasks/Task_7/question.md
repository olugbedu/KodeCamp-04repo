Task:
To strengthen your knowledge and skill with Docker and Kubernetes, create a simple application, containerize it, and deploy it to a Kubernetes cluster.

 

Steps:
 

Create a simple web application:
Use Python Programming Language to create your simple application
The application should display a simple message like "Hello, Welcome to KodeCamp DevOps Bookcamp!"
You can give your app more features if you choose to.
Dockerize the application:
Write a Dockerfile to containerize the application.
Build the Docker image and run it locally to ensure it works correctly.
Tag it and Push the Docker image to a container registry (e.g., Docker Hub).
Deploy the application to a Kubernetes cluster:
Create a Kubernetes manifest file for a Deployment to deploy the Docker image.
Deploy the app to your minikube cluster
Create a Kubernetes Service of type ClusterIP to expose the application.
Test the deployment:
Port-forward your service to a localhost port and access it through your web browser.
Verify that the application displays the expected message.
 
Submission:
Push your code to your GitHub repo and submit the link.
Include screenshots of your working application.
Share the Docker image URL from Docker Hub.
Document the steps you followed and any issues you encountered.
 
Bonus (Optional):
Configure a ConfigMap to externalize the message "Hello, Kubernetes!" and update your application to read this message from the ConfigMap.
Create a Secret to store a sensitive piece of information (e.g., a password) and update your application to use this Secret.
Links
1.

Github Link
Resources
https://kubernetes.io/docs/concepts/workloads/
https://kubernetes.io/docs/concepts/services-networking/service/
https://kubernetes.io/docs/concepts/configuration/secret/
https://kubernetes.io/docs/concepts/configuration/overview/
