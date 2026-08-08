from fastapi import FastAPI
from pydantic import BaseModel 

app=FastAPI()


@app.get("/")
def get_home():
    return{
        "message":"welcome to the Get REquest "
    }

#  old Format of Post Request :
@app.post("/post")
def home(name:str,age:int):
    return{
        "name":name,
        "age":age
    }

#  dictionary format of Post Request :
@app.post("/postdict")
def post_dict(user:dict):
    return{
        "name":user["name"],
        "age":user["age"],
        "data":user,# json data will be returned in the response
        "messages":"this is dictionary format of post request "
    }


#  New Format of Post Request :
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int

@app.post("/newpost")
def new_post(user:User):
    return{
        "name":user.name,
        "age":user.age,
        "data":user, # json data will be returned in the response
        "message":"this is new format of post request "
    }



