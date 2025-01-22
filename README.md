# AI-Powered Job Recommendation Platform

This is a simplified **AI-Powered Job Recommendation Platform** built with Flask, SQLAlchemy, and spaCy. It provides job recommendations to users based on their skills, using natural language processing to match user skills with job requirements.

## Features

- RESTful API built with Flask.
- SQLite database using SQLAlchemy ORM.
- NLP-based job recommendation using spaCy.
- Simple user and job management.
- Easy setup and configuration.

## Project Structure


## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/job-recommendation-platform.git
   cd job-recommendation-platform
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python -m spacy download en_core_web_sm
How It Works
Users and Jobs are stored in a SQLite database.
When a user requests job recommendations, their skills are matched with job requirements using spaCy's NLP similarity function.
Jobs with a similarity score above a defined threshold are recommended.
Contributing
Fork the project.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a pull request.
