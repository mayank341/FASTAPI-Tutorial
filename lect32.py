# TOPIC :RATE LIMITING + SLOWAPI +PROJECT YOUR API FROM ABUSE 

from fastapi import FastAPI,Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app=FastAPI()

#  Limiter SETUP ::
limiter=Limiter(key_func=get_remote_address)
app.state.limiter=limiter

#  error Handle :
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request:Request,exc:RateLimitExceeded):
    return JSONResponse(
        status_code=429,
           content={"message": "Too many requests, try again later"}
    )

#  Rate LImiter API :
@app.get("/data")
@limiter.limit("5/minute")
def get_data(request:Request):
    return{
        "messages":"success"
    }



