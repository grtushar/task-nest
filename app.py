import time

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.exc import OperationalError

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/tasks/*": {"origins": "*"}}, supports_credentials=True)  # Enable CORS for all routes


# Configure database connection (MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@db/tasks_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy ORM
db = SQLAlchemy(app)


# Define Task model representing a task in the database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each task
    title = db.Column(db.String(200), nullable=False)  # Task title (required)
    status = db.Column(db.String(20), default='pending')  # Task status (default is 'pending')


# Function to wait for database before creating tables
def wait_for_db():
    retries = 5  # Number of attempts
    while retries > 0:
        try:
            with app.app_context():
                db.create_all()  # Create tables only if they don't exist
            print("✅ Database is ready. Tables checked/created.")
            return
        except OperationalError:
            print("⏳ Waiting for database to be ready...")
            time.sleep(5)
            retries -= 1
    print("❌ Database connection failed after multiple attempts.")


# Ensure tables are created on first run
wait_for_db()


# ✅ Explicitly add CORS headers to responses
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response


# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()  # Fetch all tasks from database
    return jsonify([{'id': task.id, 'title': task.title, 'status': task.status} for task in tasks])


# Route to add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()  # Get task data from request body
    new_task = Task(title=data['title'])  # Create a new Task object
    db.session.add(new_task)  # Add task to database session
    db.session.commit()  # Commit changes to database
    return jsonify({'message': 'Task added successfully'}), 201


# Route to update a task (mark as completed)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)  # Fetch task by ID
    if not task:
        return jsonify({'message': 'Task not found'}), 404  # Return error if task doesn't exist
    task.status = 'completed'  # Update task status
    db.session.commit()  # Commit changes to database
    return jsonify({'message': 'Task marked as completed'})


# Route to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)  # Fetch task by ID
    if not task:
        return jsonify({'message': 'Task not found'}), 404  # Return error if task doesn't exist
    db.session.delete(task)  # Remove task from database
    db.session.commit()  # Commit deletion
    return jsonify({'message': 'Task deleted successfully'})


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Make app accessible from any IP (useful for Docker)
