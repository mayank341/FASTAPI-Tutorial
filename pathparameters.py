from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return{
        "message":"hello world "
    }

#  users Route :
@app.get("/users/{user_id}")
def users(user_id:str):
    return{
        "user_id": user_id
    }

