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
- ```server.py```: file that initialize the flask app, get the api blueprints from routes folder. Run the backend with this file. To run the backend: ```python server.py```
- ```config.py``` and ```database.py```: they are used to config and connect to database
- ```routes/```: this folder stores the create of APIs. For example ```course_routes.py``` stores the GET, POST, DELETE,... methods related to courses (create a new course, get course information, delete a course,...)


