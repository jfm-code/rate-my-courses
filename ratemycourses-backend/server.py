from flask import Flask, request, jsonify
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# api route for getting the list of courses
# the courses function will be called when a GET request is sent to the /courses api route.
# It will create the tables in the database if not exist, query the courses data and send it back to the front end. 
@app.route("/courses", methods=['GET'])
def courses():
    # connect to postgreSQL
    conn = psycopg2.connect(host=os.getenv("DBHOST"), dbname=os.getenv("DBNAME"), user=os.getenv("DBUSER"),
                            password=os.getenv("DBPASSWORD"), port=os.getenv("DBPORT"))
    cur = conn.cursor()
    

    # create the course table if not exist
    create_course_table_query = """
    CREATE TABLE IF NOT EXISTS courses (
        course_id VARCHAR(7) PRIMARY KEY,
        course_title VARCHAR(200)
    );
    """
    cur.execute(create_course_table_query)
    conn.commit()

    # create the reviews table if not exist
    create_review_table_query = """
    CREATE TABLE IF NOT EXISTS reviews (
        course_id VARCHAR(7) PRIMARY KEY,
        reviews JSONB
    );
    """
    cur.execute(create_review_table_query)
    conn.commit()

    # fetch all data in the course table
    select_query = "SELECT * FROM courses;"
    cur.execute(select_query)
    rows = cur.fetchall() # rows is a list of tuple with each tuple is a row in the course table. 

    #convert rows that is a list of tuple to dictionary type
    courses_dict={}
    
    for row in rows:
        courses_dict[row[0]] = row[1]
    
    cur.close()
    conn.close() # end connection to the database

    return jsonify(courses_dict)

# handle the request to get the review.
# the review function will be called when a GET request is sent to the /<id>/review api route.
# It will query the courses data based on the given course_id and send it back to the front end. 
@app.route("/<id>/review", methods=['GET']) 
def review(id):
    conn = psycopg2.connect(host=os.getenv("DBHOST"), dbname=os.getenv("DBNAME"), user=os.getenv("DBUSER"),
                            password=os.getenv("DBPASSWORD"), port=os.getenv("DBPORT"))
    cur = conn.cursor()
    
    # query the reviews of the course based on the course_id
    select_query = '''SELECT reviews FROM reviews WHERE course_id = %s'''
    cur.execute(select_query, (id,)) # this syntax will handle query injection
    reviews = cur.fetchall()
    conn.commit()

    cur.close()
    conn.close() # end connection to the database
    return jsonify(reviews)

if __name__ == "__main__":
    app.run(debug=True)

