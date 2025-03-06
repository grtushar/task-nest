# TaskNest - A cozy place for all your tasks

TaskNest is a simple, lightweight Task Manager application designed to help users efficiently add, view, and manage their tasks. It provides an easy-to-use interface powered by Flask and a MySQL backend, with a responsive frontend served via Nginx.

## Features

✅ Add new tasks to stay organized\
✅ View a list of all pending tasks\
✅ Mark tasks as completed\
✅ Delete tasks that are no longer needed\
✅ Fully containerized with Docker & Docker Compose

## Technologies Used

- **Backend**: Flask, Flask-SQLAlchemy
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript (served via Nginx)
- **Containerization**: Docker, Docker Compose

## Folder Structure

```
project-root/
│── app.py               # Main Flask application
│── Dockerfile           # Docker configuration for Flask app
│── docker-compose.yml   # Docker Compose setup
│── requirements.txt     # Python dependencies
│── nginx.conf           # Nginx configuration file
│── templates/           # HTML templates
│   ├── index.html       # Main UI page
│   ├── styles.css       # Stylesheet for UI

```

## Setup & Installation

### Prerequisites

Ensure you have the following installed:

- Docker & Docker Compose

### Running Locally

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/tasknest.git
   cd taskflow
   ```
2. Build and start the application using Docker Compose:
   ```sh
   docker-compose up --build
   ```
3. Open your browser and navigate to:
   ```
   http://localhost
   ```

This applies the necessary migrations if the database tables don't exist.

## API Endpoints

| Method | Endpoint    | Description              |
|--------|-------------|--------------------------|
| GET    | /tasks      | Retrieve all tasks       |
| POST   | /tasks      | Add a new task           |
| PUT    | /tasks/{id} | Mark a task as completed |
| DELETE | /tasks/{id} | Delete a task            |

## Future Enhancements

🚀 User authentication for personalized task management\
🚀 Task categories & priorities\
🚀 Due dates & reminders\
🚀 Mobile-friendly UI

## Contributors

- **grtushar** – Developer & Maintainer

## License

This project is licensed under the MIT License.

