from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import spacy

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# NLP model
nlp = spacy.load("en_core_web_sm")

# Database Models
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    required_skills = db.Column(db.String(200), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.String(200), nullable=False)

# Routes
@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([{'title': job.title, 'description': job.description, 'required_skills': job.required_skills} for job in jobs])

@app.route('/users/<int:user_id>/recommendations', methods=['GET'])
def get_recommendations(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    recommended_jobs = recommend_jobs(user)
    return jsonify([{'title': job.title, 'description': job.description} for job in recommended_jobs])

# Recommendation Logic
def recommend_jobs(user):
    user_skills_doc = nlp(user.skills.lower())
    jobs = Job.query.all()
    
    recommended_jobs = []
    for job in jobs:
        job_skills_doc = nlp(job.required_skills.lower())
        similarity = user_skills_doc.similarity(job_skills_doc)
        if similarity > 0.5:  # Threshold for recommendation
            recommended_jobs.append(job)
    
    return recommended_jobs

# Main block to run the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Initialize the database
    app.run(debug=True)
