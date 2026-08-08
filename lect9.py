from fastapi import FastAPI

from pydantic import BaseModel

app=FastAPI()

user=[]

class User(BaseModel):
    name:str
    age:int
    id:int


@app.post("/users")
def add_user(user_data:User):
    user.append(user_data)
    return{
        "message":"user added successfully",
        "data":user_data
    }   


@app.put("/users/{user_id}")
def update_user(user_id:int, user_data:User, notify:bool =False):
    if user_id<len(user):
        user[user_id]=user_data
        return{
            "message":"user updated successfully",
            "data":user_data
        }
    return{
            "messages":"user not found"
        }
    

 

#  get :
@app.get("/users/{user_id}")
def get_user():
    return{
        "messages":"list of user",
        "data":user
    }

