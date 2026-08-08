# TOPIC : STATUS CODE +CUSTOM RESPONSE +HANDLING 

from fastapi import FastAPI,HTTPException
from fastapi import status



app=FastAPI()

@app.post("/create_user",status_code= status.HTTP_201_CREATED)

def create_user():
    return{"messages":"user created successfully"}


#  get User :
@app.get("/get_user")
def get_user():
    return{
        "messages":"user fatching",
         "data":None,
         "name":"Mayanl",
         "status":"Succesful Fetching"
    }


#  Exception Handling :
@app.get("/get_user/{user_id}")
def get_user(user_id: str):
    # Simulate a scenario where the user is not found
    if user_id != "123":
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "messages": "user fetched successfully",
        "data": {"id": user_id, "name": "John Doe"}
    }
