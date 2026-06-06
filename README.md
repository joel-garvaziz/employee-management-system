# Employee Management System

A production-ready Employee Management System built using Flask, MySQL, Docker, AWS EC2, Nginx, GitHub Actions CI/CD, Amazon CloudWatch, and Let's Encrypt SSL.

This project was developed as a Cloud & DevOps Capstone Project to demonstrate full-stack application development, cloud deployment, containerization, security implementation, CI/CD automation, monitoring, and Linux server administration.

---

# Live Application

🌐 https://joel-ems.duckdns.org

---

# Project Overview

The Employee Management System provides secure user authentication and employee management functionality through a web-based interface.

The application supports role-based access control where administrators can manage employee records while standard users have restricted access.

The entire application is containerized using Docker, deployed on AWS EC2, secured with HTTPS, monitored using Amazon CloudWatch, and automatically deployed through GitHub Actions.

---

# Features

## Authentication & Authorization

* User Registration
* User Login
* User Logout
* Password Hashing using Bcrypt
* Session-Based Authentication
* Role-Based Access Control (Admin/User)
* Invalid Credentials Handling
* Access Denied Page for Unauthorized Users
* User Role Display (Admin/User)

---

## Employee Management

### Create Employee

Administrators can add new employees.

### View Employees

Administrators can view all employee records.

### Edit Employee

Administrators can update employee information.

### Delete Employee

Administrators can remove employee records.

---

## Security Features

* Password Hashing using Bcrypt
* HTTPS Encryption using Let's Encrypt SSL
* Role-Based Access Control
* Environment Variable Configuration
* Secure Session Management
* SSH Key-Based Authentication
* Nginx Reverse Proxy
* AWS Security Group Configuration

---

## Cloud & DevOps Features

* AWS EC2 Deployment
* Ubuntu 24.04 LTS Server
* Docker Containerization
* Docker Compose Orchestration
* GitHub Repository Integration
* GitHub Actions CI/CD Pipeline
* Automated Deployment
* Amazon CloudWatch Monitoring
* Custom Domain using DuckDNS
* SSL Certificate Auto Renewal

---

# Technology Stack

## Frontend

* HTML5
* Bootstrap 5

## Backend

* Python
* Flask
* SQLAlchemy
* Flask-Bcrypt

## Database

* MySQL 8

## DevOps

* Docker
* Docker Compose
* GitHub Actions

## Cloud

* AWS EC2
* Amazon CloudWatch

## Web Server

* Nginx

## DNS & SSL

* DuckDNS
* Let's Encrypt

---

# System Architecture

User Browser
↓
DuckDNS Domain
↓
HTTPS (Let's Encrypt SSL)
↓
Nginx Reverse Proxy
↓
Flask Application (Docker Container)
↓
MySQL Database (Docker Container)

Amazon CloudWatch
↓
Memory Monitoring
Disk Monitoring
Infrastructure Metrics

---

# Deployment Architecture

## Infrastructure

### AWS EC2

* Ubuntu 24.04 LTS
* Public EC2 Instance
* Security Groups Configured

### Docker Environment

#### Flask Container

* Python 3.10
* Flask Application
* SQLAlchemy ORM

#### MySQL Container

* MySQL 8
* Persistent Docker Volume Storage

### Reverse Proxy

* Nginx
* HTTPS Redirection
* SSL Termination

### Domain

* DuckDNS Dynamic DNS
* Public Domain Mapping

### SSL

* Let's Encrypt Certificate
* Automated Renewal

---

# AWS Services Used

## Amazon EC2

Used for hosting the application.

## Amazon CloudWatch

Used for:

* Memory Monitoring
* Disk Monitoring
* Infrastructure Metrics Collection

## IAM

Used for CloudWatch Agent permissions.

---

# Monitoring & Observability

Amazon CloudWatch Agent is installed and configured on the EC2 instance.

### Metrics Collected

* Memory Utilization
* Disk Utilization
* EC2 Infrastructure Metrics

### Monitoring Features

* Real-Time Metrics
* CloudWatch Dashboard
* Performance Tracking

---

# CI/CD Pipeline

GitHub Actions is used for Continuous Integration and Continuous Deployment.

## Workflow

1. Developer pushes code to GitHub.
2. GitHub Actions workflow is triggered.
3. Workflow connects to AWS EC2 using SSH.
4. Latest code is pulled.
5. Docker containers are rebuilt.
6. Existing containers are replaced.
7. Updated application is deployed automatically.

---

# Linux Administration Tasks Performed

* SSH Configuration
* EC2 Server Management
* Docker Installation
* Docker Compose Installation
* Nginx Configuration
* SSL Certificate Management
* CloudWatch Agent Configuration
* Log Monitoring
* Service Management

---

# Project Structure

employee-management-system/

├── .github/workflows/

│ └── deploy.yml

├── models/

│ ├── employee.py

│ └── user.py

├── routes/

│ ├── auth.py

│ └── employee.py

├── templates/

│ ├── login.html

│ ├── register.html

│ ├── dashboard.html

│ ├── employees.html

│ ├── add_employee.html

│ ├── edit_employee.html

│ └── access_denied.html

├── app.py

├── config.py

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── README.md

└── .gitignore

---

# Local Development Setup

## Clone Repository

git clone https://github.com/joel-garvaziz/employee-management-system.git

cd employee-management-system

## Install Dependencies

pip install -r requirements.txt

## Configure Environment Variables

Create:

.env

Configure:

DB_HOST

DB_USER

DB_PASSWORD

DB_NAME

SECRET_KEY

JWT_SECRET_KEY

## Run Application

python app.py

---

# Docker Deployment

## Build Containers

docker compose build

## Start Containers

docker compose up -d

## View Running Containers

docker ps

---

# Production URL

https://joel-ems.duckdns.org

---

# Future Enhancements

* Employee Search
* Department Management
* Salary Analytics Dashboard
* Email Notifications
* Password Reset Functionality
* AWS RDS Migration
* AWS Load Balancer Integration
* Container Orchestration using Kubernetes

---

# Author

Joel Garvaziz

Cloud & DevOps Capstone Project

2026
