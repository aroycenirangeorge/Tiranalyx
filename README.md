# Tiranalyx

### AI-Powered Log Intelligence Platform

Tiranalyx is an AI-powered log analysis platform that automatically parses application logs, identifies errors and warnings, classifies their severity, explains potential impact, and generates AI-assisted root-cause insights and recommended actions.

It is designed to reduce the time developers spend manually scanning large application logs.

## Demonstration

🔗 Live Application: http://35.154.90.3/

🔗 GitHub Repository: https://github.com/aroycenirangeorge/Tiranalyx

---

## 🚀 Features

* Upload application log files
* Automatically parse structured log entries
* Detect errors and warnings
* Classify detected issues by type and severity
* Generate log statistics
* AI-assisted problem analysis
* Generate likely causes and recommended actions
* React-based web interface
* Deployed on AWS EC2
* Automated CI/CD using GitHub Actions
* Nginx reverse proxy
* Gunicorn-based Django deployment

---

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │       Developer      │
                    │      / GitHub        │
                    └──────────┬───────────┘
                               │
                         git push
                               │
                               ▼
                    ┌──────────────────────┐
                    │   GitHub Actions      │
                    │       CI/CD           │
                    └──────────┬───────────┘
                               │
                               ▼
              ┌─────────────────────────────────┐
              │             AWS EC2             │
              │                                 │
              │        ┌───────────────┐        │
              │        │     Nginx     │        │
              │        └───────┬───────┘        │
              │                │                │
              │       ┌────────┴────────┐       │
              │       │                 │       │
              │       ▼                 ▼       │
              │  React/Vite          Gunicorn   │
              │  Frontend             Django    │
              │                           │     │
              │                           ▼     │
              │                    Log Analyzer │
              │                           │     │
              │                           ▼     │
              │                       AI Service│
              │                                 │
              └─────────────────────────────────┘
```

<img width="1699" height="926" alt="image" src="https://github.com/user-attachments/assets/b3dd9f16-e23e-4094-8581-f003bf33450a" />

---

## 🛠️ Tech Stack

### Frontend

* React
* Vite
* JavaScript
* HTML/CSS

### Backend

* Python
* Django
* Django REST Framework
* Gunicorn

### AI

* Hugging Face
* AI-assisted log analysis

### Cloud & DevOps

* AWS EC2
* Nginx
* GitHub Actions
* Linux
* systemd
* CI/CD

### Version Control

* Git
* GitHub

---

## 🔄 How It Works

### 1. Upload

The user uploads an application log file through the React interface.

### 2. Parse

The Django backend reads the log file and extracts:

* Timestamp
* Log level
* Message

### 3. Analyze

Tiranalyx identifies:

* Errors
* Warnings
* Information logs
* Issue types
* Severity
* Potential impact

### 4. AI Analysis

Detected issues are passed to the AI service to generate:

* Problem summary
* Likely cause
* Recommended actions

### 5. Display

The React frontend presents the analysis in a structured dashboard.

---

## 📊 Example

Given a log containing:

```text
ERROR Request timeout while contacting payment service
ERROR Connection refused to authentication service
WARNING Memory usage at 78%
WARNING Disk usage at 91%
```

Tiranalyx can identify:

```text
Errors: 2
Warnings: 2
Info: 3
```

and generate insights such as:

```text
Problem:
Two high-severity issues affected dependent services.

Likely Cause:
Network or service availability problems.

Recommended Actions:
- Investigate network connectivity
- Check dependent service health
- Implement retry mechanisms and exponential backoff
```

---

## 🔌 API

### Health Check

```http
GET /api/health/
```

Example response:

```json
{
  "status": "running",
  "message": "Tiranalyx backend is working!"
}
```

### Log Upload

```http
POST /api/upload/
```

Multipart form:

```text
file=<log-file>
```

---

## ☁️ Deployment

Tiranalyx is deployed on an AWS EC2 instance using:

```text
Internet
   │
   ▼
Nginx
   │
   ├── React/Vite static frontend
   │
   └── Django API
          │
          ▼
       Gunicorn
```

The Django backend runs as a `systemd` service and Nginx handles HTTP traffic and reverse proxying.

---

## 🔄 CI/CD Pipeline

Every push to the `main` branch triggers GitHub Actions.

```text
git push
   ↓
GitHub Actions
   ↓
Install Python dependencies
   ↓
Django system check
   ↓
Install Node dependencies
   ↓
Build React frontend
   ↓
SSH into AWS EC2
   ↓
Pull latest code
   ↓
Restart Gunicorn/Django
   ↓
Build frontend
   ↓
Reload Nginx
   ↓
Deployment complete
```

This allows changes pushed to GitHub to be automatically validated and deployed to the EC2 server.

---

## 📁 Project Structure

```text
Tiranalyx/
│
├── backend/
│   ├── analyzer/
│   │   ├── parser.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ai_service.py
│   │
│   ├── backend/
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   └── manage.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── ...
│   ├── package.json
│   └── vite.config.js
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── requirements.txt
└── README.md
```

---

## 🔐 Security

Sensitive credentials are not stored directly in the source code.

Environment variables and GitHub Actions Secrets are used for sensitive configuration such as:

```text
HF_TOKEN
EC2_HOST
EC2_SSH_KEY
```

---

## 🎯 Project Goals

Tiranalyx was built to demonstrate the integration of:

* Full-stack web development
* AI-assisted analysis
* Cloud deployment
* Linux server administration
* Reverse proxy configuration
* Application server deployment
* CI/CD automation

---

## 🖥️ Screenshots

Dashboard

Add your dashboard screenshot here.




Log Analysis

Add your analysis-result screenshot here.




CI/CD Pipeline

Add your GitHub Actions screenshot here.


---

## 👨‍💻 Author

**Royce Niran George A**

---

