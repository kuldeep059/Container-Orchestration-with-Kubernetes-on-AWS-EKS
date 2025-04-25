# Container Orchestration with Kubernetes on AWS EKS

This project demonstrates a basic workflow for containerizing a simple Flask application using Docker and deploying it to an Amazon Elastic Kubernetes Service (EKS) cluster.

## Overview

This repository contains the necessary files to:

* **Containerize:** Package a Python Flask application into a Docker container.
* **Orchestrate:** Deploy and manage the containerized application on a Kubernetes cluster hosted on AWS EKS.
* **Expose:** Make the application accessible externally via an AWS Load Balancer.

## Files Included

* `app.py`: A simple "Hello, World!" Flask application.
* `requirements.txt`: Lists the Python dependencies for the Flask application.
* `Dockerfile`: Defines the steps to build the Docker image for the Flask application.
* `deployment.yaml`: Kubernetes Deployment definition to manage the application's Pods.
* `service.yaml`: Kubernetes Service definition to expose the application externally using a LoadBalancer.

## Prerequisites

Before you begin, ensure you have the following installed and configured:

* **Docker:** Installed on your local machine. You should be able to build and run Docker containers.
    * [Docker Installation Guide](https://docs.docker.com/get-docker/)
* **AWS CLI:** Configured with your AWS credentials and a default region.
    * [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
    * [AWS CLI Configuration Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
* **`kubectl`:** The Kubernetes command-line tool.
    * [kubectl Installation Guide](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* **`eksctl`:** The command-line tool for creating and managing EKS clusters.
    * [eksctl Installation Guide](https://eksctl.io/installation/)
* **Docker Hub Account:** A Docker Hub account to push and store your Docker image.

## Getting Started

Follow these steps to deploy the application to your AWS EKS cluster:

1.  **Clone this repository (optional if you have your own files):**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Build the Docker Image:**
    Navigate to the directory containing the `Dockerfile` and run:
    ```bash
    docker build -t <your_dockerhub_username>/my-flask-app:v1 .
    ```
    Replace `<your_dockerhub_username>` with your Docker Hub username.

3.  **Push the Docker Image to Docker Hub:**
    Log in to Docker:
    ```bash
    docker login
    ```
    Then push the image:
    ```bash
    docker push <your_dockerhub_username>/my-flask-app:v1
    ```

4.  **Create an EKS Cluster:**
    If you don't have an EKS cluster already, create one using `eksctl`:
    ```bash
    eksctl create cluster --name my-eks-cluster --region <your_aws_region> --nodegroup-name standard-nodes --node-type t3.medium --nodes 2
    ```
    Replace `<your_aws_region>` with your desired AWS region. This step might take 10-20 minutes.

5.  **Configure `kubectl`:**
    `eksctl` usually configures `kubectl` automatically after cluster creation. Verify by running:
    ```bash
    kubectl get nodes
    ```

6.  **Apply the Kubernetes Deployment:**
    Apply the `deployment.yaml` file to create the Deployment in your EKS cluster:
    ```bash
    kubectl apply -f deployment.yaml
    ```
    **Note:** Ensure you have replaced `<your_dockerhub_username>` in the `deployment.yaml` file with your actual Docker Hub username.

7.  **Apply the Kubernetes Service:**
    Apply the `service.yaml` file to create the LoadBalancer Service:
    ```bash
    kubectl apply -f service.yaml
    ```

8.  **Access the Application:**
    Get the external IP or DNS name of the LoadBalancer:
    ```bash
    kubectl get service my-flask-app-service
    ```
    Open your web browser and navigate to the address listed under the `EXTERNAL-IP` or `LOADBALANCER INGRESS` column.

## Cleanup

To avoid incurring unnecessary AWS charges, remember to delete your EKS cluster and associated resources when you are finished:

```bash
eksctl delete cluster --name my-eks-cluster --region <your_aws_region>
