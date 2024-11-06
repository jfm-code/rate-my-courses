from flask import Blueprint, request, jsonify
from database import get_db_connection

review_bp = Blueprint("review", __name__)

@review_bp.route("/<course_id>", methods=['GET'])
def get_reviews(course_id):
    conn = get_db_connection()
    cur = conn.cursor()

    # create reviews table if it doesn't exist
    # foreign key constraint ensures that every course_id in the reviews table must exist in the courses table
    create_review_table_query = """
    CREATE TABLE IF NOT EXISTS reviews (
        review_id SERIAL PRIMARY KEY,
        course_id INTEGER NOT NULL,
        rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
        comment TEXT NOT NULL,
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
    );
    """
    cur.execute(create_review_table_query)
    conn.commit()

    # fetch reviews with given course_id
    select_query = "SELECT review_id, rating, comment FROM reviews WHERE course_id = %s"
    cur.execute(select_query, (course_id,))
    reviews = cur.fetchall()

    # results a list of dictionaries
    reviews_list = [
        {
            "review_id": row[0],
            "rating": row[1],
            "comment": row[2]
        }
        for row in reviews
    ]

    cur.close()
    conn.close()
    return jsonify(reviews_list)

@review_bp.route("/<course_id>", methods=['POST'])
def post_review(course_id):
    data = request.get_json()
    rating = data.get("rating")
    comment = data.get("comment")
    
    # Validate that necessary data is present
    if rating is None or comment is None:
        return jsonify({"error": "Rating and comment are required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    # add a new review for the given course_id
    insert_query = """
    INSERT INTO reviews (course_id, rating, comment) 
    VALUES (%s, %s, %s);
    """
    cur.execute(insert_query, (course_id, rating, comment))
    conn.commit()

    cur.close()
    conn.close()
    return jsonify({"message": "Review added successfully"}), 201

@review_bp.route("/<review_id>", methods=['DELETE'])
def delete_review(review_id):
    conn = get_db_connection()
    cur = conn.cursor()

    # delete the review based on review_id, not course_id
    delete_query = "DELETE FROM reviews WHERE review_id = %s;"
    cur.execute(delete_query, (review_id,))
    conn.commit()

    cur.close()
    conn.close()
    return jsonify({"message": "Review deleted successfully"}), 200
