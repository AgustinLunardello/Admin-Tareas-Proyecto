
---
# Task Manager with User Authentication

## Description

The Task Manager is a Python-based application that allows users to manage their tasks efficiently. It includes a user authentication system to ensure that each user can access their own tasks securely. The application uses an API to interact with the backend and store task data in a database.

## Features

- User Registration: New users can sign up by providing a unique username and password.
- User Login: Registered users can log in using their credentials to access their tasks.
- Task Creation: Authenticated users can add new tasks with details such as task name, description, and due date.
- Task Listing: Users can view a list of all their tasks with relevant information.
- Task Deletion: Users have the option to remove tasks from their list when they are completed or no longer needed.
- Task Update: Users can edit task details to keep information up-to-date.

## Requirements

- Python (version 3.11.3)
- FastAPI (version 0.97.0)
- Database (SQLite3)

## Installation

1. Clone the repository:

```
git clone https://github.com/AgustinLunardello/Admin-Tareas-Proyecto.git
cd your_project
```

2. Create a virtual environment and activate it (optional but recommended):

```
python -m venv venv
source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Run the application:

```
python app.py
```

## API Endpoints

- `POST /api/register-user`: Register a new user by providing a username and password.
- `POST /api/login`: Log in with an existing username and password to get an access token.
- `GET /api/tasks/<author>`: Retrieve all tasks associated with the authenticated user.
- `GET /api/task/<task_id>/<author>`: Retrive task associated with the authentifated user and by the task id
- `POST /api/task`: Add a new task by providing task details.
- `PUT /api/tasks/<task_id>/<author>/<new_state>`: Update an existing task by providing new details.
- `DELETE /api/tasks/<task_id>/<author>`: Delete a task by its ID.

## Usage

1. Ensure the application is running.

2. Then run the interface ```CLI\main.py```.

3. Register a new user .

4. Log in with the registered user to get an access token.

5.  After gaining access, you can to add, retrieve, update, or delete tasks.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)

---
AgustinLunardello