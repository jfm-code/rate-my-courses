Database structure:
Course table:
|---------------------------------|---------------------------|
|course_id varchar(7) PRIMARY KEY | course_title varchar(200) |
|---------------------------------|---------------------------|
|1234567                          | Computing I               |
|---------------------------------|---------------------------|
|7654321                          |Computing II               |
|---------------------------------|---------------------------|

Reviews table:
|---------------------------------|---------------------------------------------------------------|
|course_id varchar(7) PRIMARY KEY | reviews JSONB                                                 |
|---------------------------------|---------------------------------------------------------------|
|1234567                          |{"review_id_1":{"rating":"7", "comment":"some comments here"}, |
|                                 |  "review_id_2":{"rating":"8", "comment":"some comments here"}}|
|---------------------------------|---------------------------------------------------------------|
|7654321                          |{"review_id_1":{"rating":"6", "comment":"some comments here"}, |
|                                 |  "review_id_2":{"rating":"9", "comment":"some comments here"}}|
|---------------------------------|---------------------------------------------------------------|

Project Setup for Backend (Flask):
pip install Flask
pip install psycopg2
pip install python-dotenv
pip install uuid
Download Pgadmin from https://www.pgadmin.org/ and setup PostgresQL database

Flask API route:
/courses: Handle the GET request from the frond end to GET the list of courses.
/courses/<id>: Handle the GET request from the frond end to GET the list of reviews for a course.
/courses/<id>/reviews: Handle POST request from the frond end to POST a review to a course.