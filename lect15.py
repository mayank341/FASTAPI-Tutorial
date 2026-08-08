# TOPIC : SQLITE DATABASE INTEGRATION+ SETUP + SQLALCHEMY INTRO :

import sqlite3
from fastapi import FastAPI

app=FastAPI()

conn=sqlite3.connect("test.db",check_same_thread=False)

cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
    id INTEGER PRIMARY KEY,
    Title TEXT,
    Completed BOOLEAN)
""")

conn.commit()  #changes save 

@app.get("/")
def home():
    return{
        "messages":"SQL LITE Connected Fine "
    }