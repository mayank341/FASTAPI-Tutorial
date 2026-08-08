from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

todos=[]

class Todo(BaseModel):
    id:int
    title:str
    description:str
    completed:bool
    priority:str

@app.post("/add_todo")
def add_todo(todo:Todo):
    todos.append(todo)
    return{
        "Message":"Todo added Successfully",
        "data":todo
    }


#  Get api :
@app.get("/get_todo")
def get_todo():
    return{
        "message":"list of todo",
        "data":todos
    }

#  Get by id :
@app.get("/todo/{todo_id}")
def get_todo_id(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return{
                "message":"todo found",
                "data":todo
                }
    return{
        "message":"todo not found"
    }

@app.put("/todo/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return{
                "message":"todo updated successfully",
                "data":updated_todo

            }
    return{
        "message":"todo not found"
    }

#  delete a todo :
@app.delete("/todo/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos.pop(index)
            return{
                "message":"todo deleted successfully"
            }
    return{
        "message":"todo not found"
    }
