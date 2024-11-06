from flask import Flask
from flask_cors import CORS
from routes.course_routes import course_bp
from routes.review_routes import review_bp

# initialize Flask app
app = Flask(__name__)
CORS(app)  # enable CORS for all routes

# Register blueprints
# all course-related endpoints will be prefixed with /courses
app.register_blueprint(course_bp, url_prefix="/courses")
# all review-related endpoints will be prefixed with /reviews
app.register_blueprint(review_bp, url_prefix="/reviews")  

if __name__ == "__main__":
    app.run(debug=True)
