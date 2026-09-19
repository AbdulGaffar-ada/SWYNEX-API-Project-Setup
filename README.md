# API Project

A simple backend API service built using Python and FastAPI as part of Internship Task 1.

## Features

* Backend API using FastAPI
* Health-check endpoint
* Environment-based configuration
* Automatic API documentation using Swagger UI
* Local development setup instructions

## Technologies Used

* Python
* FastAPI
* Uvicorn
* python-dotenv

## Project Structure

```text
api_project/
│
├── app/
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

Make sure Python is installed on your system.

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project directory

```bash
cd api_project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root:

```env
ENVIRONMENT=development
APP_NAME=API Project
```

### 7. Start the server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Endpoints

### Home

```text
GET /
```

Returns basic information about the API.

### Health Check

```text
GET /health
```

Returns the health status of the application.

Example response:

```json
{
    "status": "healthy",
    "environment": "development"
}
```

## API Documentation

FastAPI provides interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

## Environment Configuration

The application uses a `.env` file for environment-specific configuration.

Example:

```env
ENVIRONMENT=development
APP_NAME=API Project
```

The `.env` file is excluded from Git using `.gitignore`.

## Author

Abdul Gaffar


## Task 2 - Database and CRUD

This task extends the FastAPI project by connecting the API to a MySQL database and implementing persistent CRUD operations for a Student resource.

### Technologies Added

- MySQL
- SQLAlchemy
- PyMySQL
- Pydantic validation

### Database

Database name:

    api_project_db

The application uses environment variables for database configuration.

Example:

    DB_USER=root
    DB_PASSWORD=your_mysql_password
    DB_HOST=localhost
    DB_PORT=3306
    DB_NAME=api_project_db

> Do not commit the `.env` file because it contains database credentials.

### Student CRUD API

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /students | Create a student |
| GET | /students | Get all students |
| GET | /students/{id} | Get one student |
| PUT | /students/{id} | Update a student |
| DELETE | /students/{id} | Delete a student |

### Sample Create Request

    POST /students

Request body:

    {
        "name": "Abdul Gaffar",
        "email": "abdul@example.com",
        "course": "Python"
    }

### Sample Update Request

    PUT /students/1

Request body:

    {
        "name": "Abdul Gaffar Updated",
        "email": "abdul.updated@example.com",
        "course": "FastAPI"
    }

### Validation and Error Handling

The API includes:

- Name and course length validation
- Email format validation
- Duplicate email handling
- Student not found handling
- HTTP 400, 404, and 422 responses

### Run the Project

Activate the virtual environment:

    venv\Scripts\activate

Install dependencies:

    python -m pip install -r requirements.txt

Start the server:

    python -m uvicorn app.main:app --reload

Open Swagger documentation:

    http://127.0.0.1:8000/docs

### Task 2 Learning Outcome

Through this task, I learned how to connect FastAPI with MySQL, use SQLAlchemy ORM, implement persistent CRUD operations, validate API requests, handle database errors, and test APIs using Swagger UI.