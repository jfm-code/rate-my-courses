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

## Project Setup for Backend (Flask) in the local Environement:
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
- ```database.py```: Get the connection to the database. 
- ```routes/```: this folder stores the create of APIs. For example ```course_routes.py``` stores the GET, POST, DELETE,... methods related to courses (create a new course, get course information, delete a course,...)

## API Routes:
- ```/courses```: is used to fetch the courses data from the database
- ```/courses/<course_id>/delete```: is used to delete a course from the database.
- ```/courses/<course_name>/create```: is used to add a course into the database.
- ```/reviews/<course_id>```: (GET) is used to get reviews of a course. 
- ```/reviews/<course_id>```: (POST) is used to add a review to a course.
- ```/reviews/<course_id>```: (DELETE) is used to delete a review of a course.