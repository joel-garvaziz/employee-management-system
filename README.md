# 🏢 Employee Management System

[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)

A production-ready **Employee Management System** built using Flask, MySQL, Docker, AWS EC2, Nginx, GitHub Actions CI/CD, Amazon CloudWatch, and Let's Encrypt SSL.

This project was developed as a **Cloud & DevOps Capstone Project** to demonstrate full-stack application development, cloud deployment, containerization, security implementation, CI/CD automation, monitoring, and Linux server administration.

---

## 🌐 Live Application

> **Production URL:** [https://joel-ems.duckdns.org](https://joel-ems.duckdns.org)

---

## 📝 Project Overview

The Employee Management System provides secure user authentication and employee management functionality through a web-based interface. 

The application supports **Role-Based Access Control (RBAC)** where administrators can manage employee records while standard users have restricted access. The entire application is containerized using Docker, deployed on AWS EC2, secured with HTTPS, monitored using Amazon CloudWatch, and automatically deployed through GitHub Actions.

---

## ✨ Features

### 🔐 Authentication & Authorization
* 👤 **User Registration & Login/Logout**
* 🛡️ **Password Hashing:** Secure storage using `Bcrypt`.
* ⏱️ **Session-Based Authentication:** Safe user session handling.
* 🚦 **Role-Based Access Control:** Admin vs. Standard User permissions.
* 🚫 **Error Handling:** Graceful handling of invalid credentials and custom **Access Denied** pages for unauthorized routes.
* 🏷️ **Role Display:** Dynamic UI rendering based on user role (Admin/User).

### 👥 Employee Management
* ➕ **Create Employee:** Administrators can add new employees.
* 👁️ **View Employees:** Administrators can view all employee records.
* ✏️ **Edit Employee:** New updates can be pushed to existing records by admins.
* ❌ **Delete Employee:** Administrators can permanently remove employee records.

### 🔒 Security Features
* Standardized password hashing using **Bcrypt**.
* Full **HTTPS Encryption** utilizing automated Let's Encrypt SSL certificates.
* Strict Role-Based Access Control enforcement.
* Secure **Environment Variable** configurations (no hardcoded secrets).
* **Nginx Reverse Proxy** shielding the application server.
* Tight **AWS Security Group** configurations (minimizing open ports).
* **SSH Key-Based Authentication** for server access.

### ☁️ Cloud & DevOps Features
* **AWS EC2 Deployment:** Hosted on a stable Ubuntu 24.04 LTS server.
* **Docker Containerization:** Application and database split into isolated containers.
* **Docker Compose Orchestration:** Simplified multi-container runtime management.
* **GitHub Actions CI/CD Pipeline:** Fully automated testing and deployment on git push.
* **Amazon CloudWatch Monitoring:** Real-time infrastructure tracking.
* **DuckDNS Integration:** Dynamic custom domain mapping.

---

## 🛠️ Technology Stack

| Layer | Technologies Used |
| :--- | :--- |
| **Frontend** | `HTML5`, `Bootstrap 5` |
| **Backend** | `Python`, `Flask`, `SQLAlchemy`, `Flask-Bcrypt` |
| **Database** | `MySQL 8` |
| **DevOps & Containers** | `Docker`, `Docker Compose` |
| **CI/CD** | `GitHub Actions` |
| **Cloud Provider** | `AWS EC2`, `Amazon CloudWatch` |
| **Web Server** | `Nginx` |
| **DNS & SSL** | `DuckDNS`, `Let's Encrypt` |

---

## 📐 System Architecture

```mermaid
graph TD
    User([User Browser]) -->|HTTPS| Duck[DuckDNS Domain]
    Duck -->|SSL Termination| Nginx[Nginx Reverse Proxy]
    Nginx -->|Proxy Pass| Flask[Flask App Container]
    Flask -->|SQLAlchemy ORM| MySQL[(MySQL Container)]
    
    subgraph AWS Cloud Watch Monitoring
        Flask -.-> CW[CloudWatch Agent]
        MySQL -.-> CW
        CW --> Dash[CloudWatch Dashboard]
    end

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
Memory Monitoring / Disk Monitoring / Infrastructure Metrics

🏗️ Deployment Architecture
Infrastructure:

AWS EC2 Single Instance running Ubuntu 24.04 LTS.

Strict Public Security Groups (Only HTTP/HTTPS and specific SSH ingress allowed).

Docker Environment:

Flask Container: Python 3.10 runtime environment utilizing SQLAlchemy ORM.

MySQL Container: MySQL 8 image running with persistent Docker volume attachments to protect data integrity.

Reverse Proxy & SSL:

Nginx: Functions as a reverse proxy handling HTTPS redirection and SSL termination.

Let's Encrypt: Provisions SSL certificates alongside an automated background cron job for renewal.

📊 AWS Services Used
💻 Amazon EC2
Used for hosting the core application backend, database containers, and web proxy.

📈 Amazon CloudWatch
Installed and configured via the CloudWatch Agent on the EC2 instance to gather:

Real-Time Memory Utilization

Disk Utilization / Storage Capacity Metrics

EC2 Infrastructure Metrics & Interactive Dashboards

🆔 IAM
Utilized to delegate tight, least-privilege permissions specifically for the CloudWatch Agent to ship logs and metrics.

🚀 CI/CD Pipeline Workflow
[ Developer Pushes Code ] ──> [ Triggers GitHub Actions ] ──> [ SSH Connection to EC2 ]
                                                                       │
[ Rebuilt & Live Application ] <── [ Replace Old Containers ] <── [ Pull Latest Code ]
Developer pushes code changes to the GitHub repository.

The GitHub Actions workflow triggers automatically.

The workflow securely authenticates with the AWS EC2 instance over SSH.

The server pulls the latest code directly from the main branch.

Docker containers are dynamically rebuilt and replaced with zero manual interference.

🐧 Linux Administration Tasks Performed
⚙️ Advanced SSH configurations and port security.

📦 Production-grade Docker & Docker Compose setup.

🌐 Custom Nginx reverse proxy configuration.

🔑 Automated SSL generation and renewal script automation.

📉 CloudWatch Agent script configuration and daemon setups.

📁 System log monitoring and service health configuration.

📂 Project Structure
Plaintext
employee-management-system/
├── .github/workflows/
│   └── deploy.yml          # CI/CD Deployment Workflow
├── models/
│   ├── employee.py         # Employee Database Model
│   └── user.py             # User/Auth Database Model
├── routes/
│   ├── auth.py             # Authentication Routes
│   └── employee.py         # Employee Management Routes
├── templates/              # HTML Frontend Templates
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── employees.html
│   ├── add_employee.html
│   ├── edit_employee.html
│   └── access_denied.html
├── app.py                  # Application Entrypoint
├── config.py               # Application Configurations
├── Dockerfile              # App Containerization Config
├── docker-compose.yml      # Multi-container Orchestrating Specs
├── requirements.txt        # Python App Dependencies
├── README.md
└── .gitignore
💻 Local Development Setup
1. Clone Repository
Bash
git clone [https://github.com/joel-garvaziz/employee-management-system.git](https://github.com/joel-garvaziz/employee-management-system.git)
cd employee-management-system
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Configure Environment Variables
Create a local .env file in the root directory and add the following keys:

Code snippet
DB_HOST=localhost
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
SECRET_KEY=your_super_secret_flask_key
JWT_SECRET_KEY=your_jwt_secret_key
4. Run Application
Bash
python app.py
🐳 Docker Production Deployment
Build Containers
Bash
docker compose build
Start Containers (Detached Mode)
Bash
docker compose up -d
View Running Containers
Bash
docker ps
🔮 Future Enhancements
🔍 Advanced Querying: Add an employee search and multi-tiered filtering system.

🏢 Department Management: Introduce organization structure handling.

📊 Analytics Dashboard: Build graphical representations of dynamic salary data.

✉️ Email Notifications: Send automated welcome alerts and updates.

🔄 Self-Service: Password reset workflows via secure email links.

☁️ AWS RDS Migration: Offload database management to an Amazon RDS MySQL instance.

⚖️ High Availability: Implement an AWS Application Load Balancer with Multi-AZ deployments.

☸️ Orchestration: Transition infrastructure workloads to a Kubernetes cluster.

✍️ Author
Joel Garvaziz

Cloud & DevOps Capstone Project — 2026
