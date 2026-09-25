# ☁️ Cloud-Based CI/CD Pipeline for Automated Application Deployment

![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![AWS](https://img.shields.io/badge/AWS-EC2-orange)
![Architecture](https://img.shields.io/badge/Architecture-ARM64-green)

## 📌 Project Overview

This project demonstrates a **cloud-based Continuous Integration and Continuous Deployment (CI/CD) pipeline** for automatically testing, containerizing, and deploying a Flask web application.

Whenever new code is pushed to the GitHub repository, the CI/CD pipeline automatically:

1. Installs the required dependencies.
2. Runs automated tests using Pytest.
3. Builds an ARM64 Docker image.
4. Pushes the Docker image to Docker Hub.
5. Authenticates with AWS using OpenID Connect (OIDC).
6. Uses AWS Systems Manager (SSM) to communicate with the EC2 instance.
7. Pulls the latest Docker image on EC2.
8. Stops the previous container.
9. Starts the updated container.
10. Makes the updated application available through the EC2 server.

The project eliminates the need for manually building and deploying the application after every code change.

---

# 🏗️ System Architecture

```mermaid
flowchart LR
    A[👨‍💻 Developer] -->|git push| B[GitHub Repository]

    B --> C[GitHub Actions]

    C --> D[Install Dependencies]
    D --> E[Pytest Automated Tests]
    E --> F[Build ARM64 Docker Image]
    F --> G[Docker Hub]

    G --> H[AWS OIDC Authentication]
    H --> I[AWS Systems Manager]

    I --> J[Amazon EC2]
    J --> K[Docker Container]
    K --> L[Flask Web Application]