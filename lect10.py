# Topic : RESPONSE mODELS +DATA VALIDATION +HIDE SENSATIVIE DATA:

from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    email:str
    password:str

class UserResponseModel(BaseModel):
    name:str
    email:str

#  temporary databases for storing users data:
users=[]

@app.post("/create_user")
def create_user(user:User):
    users.append(user)
    return{
        "message":"user created successfully",
        "data":user

    }

@app.get("/get_user",response_model= list[UserResponseModel])
def get_user():
    return users    
