
# Simple HR Backend API

## Description
A simple RESTful backend API for managing employee data, built with Python, Flask, and SQLAlchemy.

## Technologies Used
* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* REST APIs
* Postman (For API's testing)

## Features
* Create new employee records (POST /employees)
* View all employee records (GET /employees)
* View a specific employee record by ID (GET /employees/{id})
* Update an existing employee record by ID (PUT /employees/{id})
* Delete an employee record by ID (DELETE /employees/{id})

## Setup and Installation
* Prerequisites (Python >= 3.10 installed)
* Clone the repository: `git clone [Your GitHub Repo URL]`
* Navigate to the project directory: `cd your-repo-name`
* Create a virtual environment: `python -m venv hr_env`
* Activate the virtual environment:
    * On Windows: `.\hr_env\Scripts\activate`
    * On macOS/Linux: `source hr_env/bin/activate`
* Install dependencies: `pip install -r requirements.txt` 
* Initialize the database:
    ```bash
    python app.py # This will run the db.create_all() part
    ```
* Run the application: `python app.py`

## How to Use the API
[how to interact with API endpoints.]
* Base URL: `http://127.0.0.1:5000`
* Endpoint: `/employees`
* **GET /employees:** Retrieve all employees.
    * Example Request: `GET http://127.0.0.1:5000/employees`
    * Example Response: `[...]` (Show a sample JSON response)
* **POST /employees:** Create a new employee.
    * Example Request: (Show a `curl` command or Postman screenshot)
    * Example Request Body (JSON): `{ "name": "...", "department": "...", ... }`
    * Example Response: `{ "message": "...", "id": ... }`
* **GET /employees/{id}:** Retrieve a specific employee by ID.
    * Example Request: `GET http://127.0.0.1:5000/employees/1`
    * Example Response: `{ "id": 1, "name": "...", ... }`
* **PUT /employees/{id}:** Update a specific employee by ID.
    * Example Request: (Show a `curl` command or Postman screenshot)
    * Example Request Body (JSON): `{ "department": "...", "age": ... }`
    * Example Response: `{ "message": "..." }`
* **DELETE /employees/{id}:** Delete a specific employee by ID.
    * Example Request: (Show a `curl` command or Postman screenshot)
    * Example Response: `{ "message": "..." }`

## Code Structure
* `app.py`: Contains the main Flask application, database models, and API routes.
* `site.db`: SQLite database file (this is generated and not committed to Git).
* `requirements.txt`: Lists project dependencies.

## [github.com/AnkitV15]