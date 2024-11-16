from flask import Flask
from flask_cors import CORS
from routes.course_routes import course_bp
from routes.review_routes import review_bp
import os
from dotenv import load_dotenv

load_dotenv()

# initialize Flask app
app = Flask(__name__)
CORS(app,  resources={r"/*": {"origins": os.getenv("FEDOMAIN")}})  # enable CORS for requests from the domain host in frontend

# Register blueprints
# all course-related endpoints will be prefixed with /courses
app.register_blueprint(course_bp, url_prefix="/courses")
# all review-related endpoints will be prefixed with /reviews
app.register_blueprint(review_bp, url_prefix="/reviews")  

if __name__ == "__main__":
    app.run(debug=True)
