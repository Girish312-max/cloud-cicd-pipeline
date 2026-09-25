# Cloud-Based CI/CD Pipeline for Automated Application Deployment

## 📌 Project Overview

This project demonstrates a cloud-based Continuous Integration and Continuous Deployment (CI/CD) pipeline for automatically building, testing, containerizing, and deploying a Flask web application.

Whenever new code is pushed to GitHub, GitHub Actions automatically runs the application tests, builds an ARM64 Docker image, pushes the image to Docker Hub, and deploys the latest version to an AWS EC2 instance using AWS Systems Manager.

## 🏗️ Architecture

Developer
   ↓
GitHub Repository
   ↓
GitHub Actions
   ↓
Automated Testing
   ↓
Docker ARM64 Build
   ↓
Docker Hub
   ↓
AWS OIDC Authentication
   ↓
AWS Systems Manager
   ↓
Amazon EC2
   ↓
Docker Container
   ↓
Live Flask Application

## 🛠️ Technologies Used

- Python
- Flask
- Pytest
- Git
- GitHub
- GitHub Actions
- Docker
- Docker Hub
- Amazon EC2
- AWS Systems Manager (SSM)
- AWS IAM
- AWS OIDC

## ✨ Features

- Automated application testing
- Automated Docker image building
- ARM64 Docker image support
- Automatic Docker Hub deployment
- Secure GitHub-to-AWS authentication using OIDC
- Automatic EC2 deployment using AWS Systems Manager
- Docker container restart on deployment
- Continuous deployment after every push to the `main` branch

## 🧪 Automated Testing

The project uses Pytest to verify that the Flask application is working correctly.

The test checks:

- HTTP status code is 200
- Expected application title is present
- Application running status is present

Run tests locally:

```bash
pytest