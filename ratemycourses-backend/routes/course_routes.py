from flask import Blueprint, jsonify
from database import get_db_connection

course_bp = Blueprint("course", __name__)

@course_bp.route("/", methods=['GET'])
def get_courses():
    conn = get_db_connection()
    cur = conn.cursor()

    # create courses table if it doesn't exist
    create_course_table_query = """
    CREATE TABLE IF NOT EXISTS courses (
        course_id SERIAL PRIMARY KEY,
        course_title VARCHAR(200)
    );
    """
    cur.execute(create_course_table_query)
    conn.commit()

    # fetch all courses
    select_query = "SELECT * FROM courses;"
    cur.execute(select_query)
    rows = cur.fetchall() # rows is a list of tuple with each tuple is a row in the course table. 

    #convert rows that is a list of tuple to dictionary type
    courses_dict={}

    for row in rows:
        course_id = row[0]
        course_name = row[1]
        courses_dict[course_id] = course_name

    cur.close()
    conn.close() # end connection to the database

    return jsonify(courses_dict)
