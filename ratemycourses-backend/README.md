# RateMyCourses Website (Backend)

We use Flask for backend and PostgreSQL for database

## Database structure:
1. **Course table**:

|course_id SERIAL PRIMARY KEY     | course_title varchar(200) |
|---------------------------------|---------------------------|
|              123                | Computing I               |
|              124                | Computing II              |

2. **Review table**:

|review_id SERIAL PRIMARY KEY     |  course_id  |  rating  |  comment                             |
|---------------------------------|-------------|----------|--------------------------------------|
|              1                  |     123     |    4     |   The course is pretty good          |
|              2                  |     124     |    2     |   The course is pretty good          |
|              3                  |     123     |    1     |   The course is pretty good          |

## Project Setup for Backend (Flask)
```
pip install Flask
pip install psycopg2
pip install python-dotenv
pip install uuid
pip install flask-cors
```
Download Pgadmin from https://www.pgadmin.org/ and setup PostgresQL database

Create .env file for the DBHOST, DBNAME, DBUSER, DBPASSWORD, DBPORT and put in the information to connect the backend to the PostgreSQL on the computer

## Notes
```conn.commit()``` is used to save changes to the database when you’re performing data modification operations like INSERT, UPDATE, or DELETE

**Files:**
- ```requirements.txt```: file that contains required libraries/dependencies to run the backend. Install by ```pip install -r requirements.txt```
- ```.env```: file that stores the information to connect to local database (example below)
    ```
    DBHOST=nameofhost
    DBNAME=databasename
    DBUSER=username
    DBPASSWORD=databasepassword
    DBPORT=databaseport
    FEDOMAIN=frontendURLtoenableCORS
    ```
- ```app.py```: before this file is named ```server.py```, but then changed to ```app.py``` so that I can run by doing ```flask run``` instead of ```python server.py```. This file initializes the flask app, get the api blueprints from routes folder.
- ```config.py``` and ```database.py```: they are used to config and connect to database
- ```routes/```: this folder stores the create of APIs. For example ```course_routes.py``` stores the GET, POST, DELETE,... methods related to courses (create a new course, get course information, delete a course,...)

## Host Backend on EC2
- Step 1: Make sure the frontend is working first
- Step 2: Launch an EC2 instance, download the .pem file
- Step 3: Add a security rule a rule to allow inbound rule SSH - TCP - port 22 and 5000 (source 0.0.0.0/0)
- Step 4: Put the .pem file inside the backend folder, open terminal, connect VM with ```ssh -i "rate_my_courses_key.pem" ec2-user@ec2-54-234-159-24.compute-1.amazonaws.com``` (open VS Code for easier interaction)
- Step 5: Clone the repo to the VM with ```git clone --branch dev <repository-url>``` or ```git clone <repository-url>```, use the github username and PAT token to login (not the usual github password). The PAT token can be created in github.
- Step 6: Install dependencies on VM (choose the command according to the type of VM we chose when launch instance)
    - For Amazon Linux 2:
        ```
        sudo yum update -y
        sudo yum install python3 -y
        sudo yum install python3-pip -y
        sudo yum install postgresql-devel -y
        ```
    - For Amazon Linux 2023:
        ```
        sudo dnf update -y
        sudo dnf install python3 -y
        sudo dnf install python3-pip -y
        sudo dnf install postgresql-devel -y
        ```
    - For Ubuntu:
        ```
        sudo apt update -y
        sudo apt install python3 python3-pip -y
        sudo apt install libpq-dev -y
        ```
    - Some more to install:
        ```
        python3 -m pip install --upgrade pip
        python3 -m pip install virtualenv
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        ```
- Step 7: Set up the database - Create RDS instance, connect with the EC2 VM that host the backend
- Step 8: Update the ```.env``` file to connect with RDS database
    ```
    DBHOST=RDS_endpoint (e.g ratemycourses-database.cluster-blablabla.us-east-1.rds.amazonaws.com)
    DBNAME=postgres (master username)
    DBUSER=postgres (by default)
    DBPASSWORD=password_generate_by_RDS (master password)
    DBPORT=5432
    FEDOMAIN=link_of_frontend
    ```
- Step 9: Run the backend with ```flask run``` and test the API with Postman (can enable CORS everywhere temporarily if we need to fix CORS)
- Step 10: Get the public IPv4 of EC2, for example if this is URL when we run ```flask run```: ```http://127.0.0.1:5000```, and the public IPv4 of EC2 is ```172.31.93.160``` then the API endpoint URL will be: ```http://172.31.93.160:5000```. Paste this new API endpoint URL into Amplify environment variable so that frontend call the right API endpoint.