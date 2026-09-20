from pydantic import BaseModel,EmailStr,Field,validator
class StudentCreate(BaseModel):
    name:str=Field(...,min_length=2,max_length=100)
    email:EmailStr
    course:str=Field(...,min_length=2,max_length=100)

    @validator("name","course")
    def validate_text(cls,value):
        value=value.strip()
        if not value:
            raise ValueError("Fields cannot be empty or contain only spaces")
        return value
class StudentUpdate(BaseModel):
    name:str=Field(...,min_length=2,max_length=100)
    email:EmailStr
    course:str=Field(...,min_length=2,max_length=100)

    @validator("name","course")
    def validate_text(cls,value):
        value=value.strip()
        if not value:
            raise ValueError("Fields cannot be empty or cannot conatin spaces")
        return value