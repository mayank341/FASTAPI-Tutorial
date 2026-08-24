# TOPIC :   API Testing with Pytest + FastAPI | Test Endpoints

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello Mayank"
    }

@app.get("/add")
def add(a: int, b: int):
    return {
        "result": a + b
    }
