# EXCEPTION HANDLING + HTTP EXCEPTION +GLOBAL ERROR HANDLES 

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()


# Custom Exception
class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name


# API
@app.get("/user/{name}")
def get_user(name: str):
    if name != "Mayank":
        raise UserNotFoundException(name)

    return {
        "name": "Mayank",
        "age": 22
    }


# Global Exception Handler
@app.exception_handler(UserNotFoundException)
async def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "message": f"User '{exc.name}' not found",
            "status": "error"
        }
    )

#Exception Handling :
# @app.get("/user/{user_id}")
# def get_user(user_id:int):
#     if user_id!=1:
#         raise HTTPException(
#             status_code=404,
#             detail="user not Found"
#         )
#     return{
#         "id":1,
#         "name":"Mayank"
#     }
