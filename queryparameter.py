from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def home():
    return{
        "message":"hello world "
    }

#  Optional query parameters :
@app.get("/users")
def home(name: str= None ):
    return{"Name": f'My name is {name}'}

#  Optional query parametrs :
@app.get("/product")
def get_user(limit:int =100):
    return{
        "limit":limit
    }

# Multiple Query Paramters :
@app.get("/items")
def get_items(name:str =None, price:int =0):
    return{
        "name": name,
        "price": price
    }
