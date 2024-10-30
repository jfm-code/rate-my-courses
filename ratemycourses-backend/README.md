# RateMyCourses Website (Backend)

## Overview

This project is a web-based application for reviewing and rating courses, similar to RateMyProfessors. It uses **Vue.js** for the frontend, **Flask** for the backend, and **PostgreSQL** for the database. The application is hosted on **AWS** with a CI/CD pipeline for automated build and deployment, using AWS services like **EC2**, **S3**, **RDS**, **CloudFormation**, and **CodePipeline**.

## Database structure:
1. **Course table**:

|course_id varchar(7) PRIMARY KEY | course_title varchar(200) |
|---------------------------------|---------------------------|
|1234567                          | Computing I               |
|7654321                          |Computing II               |

2. **Review table**:

|course_id varchar(7) PRIMARY KEY | reviews JSONB                                                 |
|---------------------------------|---------------------------------------------------------------|
|1234567                          |{"review_id_1":{"rating":"7", "comment":"some comments here"}, |
|                                 |  "review_id_2":{"rating":"8", "comment":"some comments here"}}|
|7654321                          |{"review_id_1":{"rating":"6", "comment":"some comments here"}, |
|                                 |  "review_id_2":{"rating":"9", "comment":"some comments here"}}|


## Project Setup for Backend (Flask)
```
pip install Flask
pip install psycopg2
pip install python-dotenv
pip install uuid
pip install flask-cors
```
Download Pgadmin from https://www.pgadmin.org/ and setup PostgresQL database

Create .env file for the DBHOST, DBNAME, DBUSER, DBPASSWORD, DBPORT

## Notes
```conn.commit()``` is used to save changes to the database when you’re performing data modification operations like INSERT, UPDATE, or DELETE

Flask API route:
- /courses: Handle the GET request from the frond end to GET the list of courses.
- /courses/<id>: Handle the GET request from the frond end to GET the list of reviews for a course.
- /courses/<id>/reviews: Handle POST request from the frond end to POST a review to a course.

To run the backend: ```python server.py```
