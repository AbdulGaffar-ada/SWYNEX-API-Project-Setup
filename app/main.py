from fastapi import FastAPI,Depends,HTTPException,Security
from fastapi.security import APIKeyHeader
import os
from dotenv import load_dotenv
from .database import engine, Base
from . import models
from sqlalchemy.orm import Session
from .database import get_db
from .models import Student
from .schemas import StudentCreate,StudentUpdate
from sqlalchemy.exc import IntegrityError

load_dotenv()

API_KEY=os.getenv("API_KEY")
api_key_header=APIKeyHeader(name="X-API-Key",auto_error=False)
def verify_api_key(api_key:str=Security(api_key_header)):
    if not api_key:
        raise HTTPException(
            status_code=401,
            detail={
                "success":False,
                "error":"API key is required"
            }
        )
    if api_key!=API_KEY:
        raise HTTPException(
            status_code=401,
            detail={
                "success":False,
                "error":"Invalid API key"
            }
        )
    return api_key

def error_response(message):
    return {
        "success":False,
        "error":message
    }

app_name=os.getenv("APP_NAME","API Project")
environment=os.getenv("ENVIRONMENT","development")
app=FastAPI(
    title="API PROJECT",
    description="Backend API for Internship Task1",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

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

@app.get("/db-test")
def database_test():
    try:
        with engine.connect() as connection:
            return {"database":"connected"}
    except Exception as e:
        return {"database":"connection failed","error":str(e)}

@app.post("/students")
def create_student(student:StudentCreate,db:Session=Depends(get_db),api_key:str=Depends(verify_api_key)):
    new_student=Student(
        name=student.name,
        email=student.email,
        course=student.course
    )
    try:
        db.add(new_student)
        db.commit()
        db.refresh(new_student)

        return new_student
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400,detail=error_response("Email already exists"))

@app.get("/students")
def get_students(db:Session=Depends(get_db),api_key:str=Depends(verify_api_key)):
    return db.query(Student).all()

@app.get("/students/{student_id}")
def get_student(student_id:int,db:Session=Depends(get_db),api_key:str=Depends(verify_api_key)):
    student=db.query(Student).filter(Student.id==student_id).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            detail=error_response("Student not found")
        )
    return student

@app.put("/students/{student_id}")
def update_student(student:StudentUpdate,student_id:int,db:Session=Depends(get_db),api_key:str=Depends(verify_api_key)):
    existing_student=db.query(Student).filter(Student.id==student_id).first()
    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail=error_response("Student not found")
        )
    existing_student.name=student.name
    existing_student.email=student.email
    existing_student.course=student.course
    db.commit()
    db.refresh(existing_student)
    return existing_student

@app.delete("/students/{student_id}")
def delete_student(student_id:int,db:Session=Depends(get_db),api_key:str=Depends(verify_api_key)):
    student=db.query(Student).filter(Student.id==student_id).first()
    if student is None:
        raise HTTPException(status_code=404,detail=error_response("Student not found"))
    db.delete(student)
    db.commit()
    return {
        "message":"Student deleted successfully"
    }