from fastapi import FastAPI

from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    email:str
    password:str
    age:int 

#  simple pydantic model for user creation :

@app.post("/create_user")
def createuser(user:User):
    return{
        "message":"user created successfully",
        "data":user
    }

# Nested Pydanrtic Model for User Creation :
class Address(BaseModel):
    city:str
    state:str
    country:str

class userWithAddress(BaseModel):
    name:str
    email:str
    password:str
    age:int
    pincode:int
    address:Address


@app.post("/create_user_with_address")
def create_user_with_address(user:userWithAddress):
    return{
        "message":"user created succesfuully with address",
        "data":user
    }
