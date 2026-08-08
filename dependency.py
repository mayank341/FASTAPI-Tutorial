# TOPIC : DEPENDENCY iNJECTION + DEPENDS()+ AUTH EXAMPLE :-

from fastapi import FastAPI,Depends,Header,HTTPException,status

app=FastAPI()

def custom_logic():
    return{
        "messages":"Dependency function exceuted "
    }

@app.get("/user")
def get_user(user=Depends(custom_logic)):
    return user

def get_curr_user():
    return{
        "name":"Mayank"
    }

@app.get("/profile")
def profile_user(user=Depends(get_curr_user)):
    return user


@app.get("/dashboard")
def dashbooard(user=Depends(get_curr_user)):
    return user


def verify_token(token: str=Header(None)):
    if token!="mysecrettoken":
        raise HTTPException(
            detail="Unauthorized",
            status_code=401
        )
    return{
        "user":"Authorized User"
    }


@app.get("/secure")
def auth(user=Depends(verify_token)):
    return {
        "messages":"Secure data access",
        "user":user
    }