from flask import Flask, request, jsonify
import uuid, os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# api route for getting the list of courses
@app.route("/courses", methods=['GET'])
def courses():
    # connect to postgreSQL
    conn = psycopg2.connect(host=os.getenv("DBHOST"), dbname=os.getenv("DBNAME"), user=os.getenv("DBUSER"),
                            password=os.getenv("DBPASSWORD"), port=os.getenv("DBPORT"))
    cur = conn.cursor()
    

    # create course table if not exist
    create_course_table_query = """
    CREATE TABLE IF NOT EXISTS courses (
        course_id VARCHAR(7) PRIMARY KEY,
        course_title VARCHAR(200)
    );
    """
    cur.execute(create_course_table_query)
    conn.commit()

    # create course table if not exist
    create_review_table_query = """
    CREATE TABLE IF NOT EXISTS courses (
        course_id VARCHAR(7) PRIMARY KEY,
        course_title VARCHAR(200)
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
    print(courses_dict)
    return jsonify(courses_dict)

if __name__ == "__main__":
    app.run(debug=True)
