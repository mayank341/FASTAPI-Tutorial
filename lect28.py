#  IN Python we can get third party api by doing this :
# import requests
# response=requests.get("https://jsonplaceholder.typicode.com/posts")

# data=response.json()
# print(data) # full data 
# print(data[:2])

# ____________________________________________
from fastapi import FastAPI,HTTPException
import requests

app=FastAPI()

# Get all the data :
@app.get("/posts")
def get_posts():
    url="https://jsonplaceholder.typicode.com/posts/"
    response=requests.get(url)
    return response.json()

#  Single Post Get :
@app.get("/posts/{post_id}")
def get_posts(post_id:int):
    url=f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response=requests.get(url)

    if response.status_code!=200:
        raise HTTPException(status_code=404,detail="Page Not Found")
    
    return response.json()
