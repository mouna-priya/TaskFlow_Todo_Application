# TaskFlow - Todo App

TaskFlow is a simple, intuitive, and user-friendly task management application built with Flask and MongoDB. It allows users to add, edit, delete, and manage tasks efficiently with a sleek UI.

---

## Features

- *Add Tasks:* Create tasks with descriptions, dates, and times.
- *Edit Tasks:* Update existing tasks.
- *Delete Tasks:* Remove unwanted tasks.
- *Mark Tasks as Completed:* Toggle task completion status.
- *Clear All Tasks:* Easily delete all tasks.
- *Task Persistence:* Uses MongoDB to store tasks.
- *Mongo Express Integration:* Web interface to manage MongoDB collections.

---

## Tech Stack

- *Backend:* Python with Flask
- *Frontend:* HTML, Bootstrap
- *Database:* MongoDB
- *Containerization:* Docker and Docker Compose

---

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Docker
- Docker Compose

### Clone the Repository

bash
git clone <repository-url>
cd taskflow-todo-app


### Build and Run the Application

1. Build and start the services:
   bash
   docker-compose up --build
   

2. Access the application at [http://localhost:5000](http://localhost:5000).
3. Access Mongo Express at [http://localhost:8081](http://localhost:8081).

### Stopping the Application

bash
docker-compose down


---

## Environment Variables

Create a .env file for storing environment variables:


MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=example
ME_CONFIG_BASICAUTH_USERNAME=admin
ME_CONFIG_BASICAUTH_PASSWORD=admin123


---

## Project Structure


├── app.py              # Main Flask application
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Docker Compose configuration
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates
├── static/              # Static CSS files
└── .gitignore           # Ignored files for version control


---

## API Routes

- *Home Page:* GET /
- *Add Task:* POST /add
- *Edit Task:* GET, POST /edit/<task_id>
- *Delete Task:* GET /delete/<task_id>
- *Toggle Task Status:* POST /check/<task_id>
- *Clear All Tasks:* GET /clear_all

---

## Future Improvements

- User authentication for multiple users.
- Task categories and priorities.
- Task reminder notifications.
- UI enhancements.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and create pull requests.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Happy tasking with *TaskFlow*! 🎉