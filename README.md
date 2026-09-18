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
