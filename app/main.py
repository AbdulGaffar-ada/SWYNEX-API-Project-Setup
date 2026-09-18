from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()
app_name=os.getenv("APP_NAME","API Project")
environment=os.getenv("ENVIRONMENT","development")
app=FastAPI(
    title="API PROJECT",
    description="Backend API for Internship Task1",
    version="1.0.0"
)
@app.get("/")
def home():
    return {
        "message":"API is running",
        "application":app_name,
        "environment":environment

    }
@app.get("/health")
def health_check():
    return {
        "status":"healthy",
        "environment":environment
    }