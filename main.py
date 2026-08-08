

from fastapi import FastAPI
 
app = FastAPI()  # app becomes an instance of FastAPI class,object 

@app.get("/")
def home():
    return{
        "message": "hello world using venv "
    }

# about ROute :
@app.get("/users")
def users():
    return{
        "message": "List of users"
    }

#  about the page route :
@app.get("/about")
def about():
    return {
        "message":"this is about page "
    }

