
# RateMyCourses Website

## Overview

This project is a web-based application for reviewing and rating courses, similar to RateMyProfessors. It uses **Vue.js** for the frontend, **Flask** for the backend, and **PostgreSQL** for the database. The application is hosted on **AWS** with a CI/CD pipeline for automated build and deployment, using AWS services like **EC2**, **S3**, **RDS**, **CloudFormation**, and **CodePipeline**.

## Project Setup

### 1. Frontend (Vue.js)

**Main roles:**
- Makes requests to backend endpoints using the URLs provided by the backend.
- Processes the data received from the backend and renders it in the user interface.

```
npm install -g @vue/cli
vue create ratemycourses-frontend
npm install axios
```
When creating the vue project, choose [Vue 3] babel, eslint and Use Yarn


### 2. Backend (Flask)

**Main roles:**
- Creates and serves endpoints (/courses and /<id>/review) that handle HTTP requests.
- Defines what data is returned by these endpoints (like course information and reviews).
- Handles database interactions and any server-side logic, ensuring the data is available for the frontend.

```
pip install Flask flask-cors psycopg2
```

#### Example structure for Flask endpoints:

- `/api/courses`: GET all courses
- `/api/courses/<id>`: GET, PUT, DELETE specific course
- `/api/courses/<id>/reviews`: POST review for a course

#### Enable CORS in Flask:

```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

### 3. Database (AWS RDS)

#### Create PostgreSQL Database:

- Go to AWS Management Console → RDS → Create Database.
- Choose PostgreSQL, configure instance settings, and set up security groups.

#### Connect Flask to RDS:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@hostname/dbname'
```

### 4. Hosting Backend (EC2)

#### Launch EC2 Instance:

- Choose Amazon Linux/Ubuntu as the OS.
- Set up security groups to allow HTTP, HTTPS, and SSH.

#### Install Flask and PostgreSQL on EC2:

```bash
sudo apt update
sudo apt install python3-pip postgresql
pip3 install Flask psycopg2
```

## Summary of Tools

- **Frontend**: Vue.js
- **Backend**: Flask
- **Database**: PostgreSQL (AWS RDS)
- **Hosting**: EC2 (Backend), S3/EC2 (Frontend)
- **CI/CD**: CodePipeline + CodeBuild
- **Infrastructure Automation**: CloudFormation
- **Domain & SSL**: Route 53 + AWS ACM
