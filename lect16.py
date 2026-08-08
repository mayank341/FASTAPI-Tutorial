# TOPIC :CRUD OPERATION WITH SQLALCHEMY DATABSES 
# LECT16-20

from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session


# --------------------------------------------------
# 1. DATABASE URL
# --------------------------------------------------
 
DATABASE_URL = "sqlite:///./test2.db"


# --------------------------------------------------
# 2. CREATE DATABASE ENGINE
# --------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# --------------------------------------------------
# 3. CREATE SESSION
# --------------------------------------------------

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


# --------------------------------------------------
# 4. CREATE BASE CLASS
# --------------------------------------------------

Base = declarative_base()
# --------------------------------------------------
# 5. CREATE MODEL / TABLE
# --------------------------------------------------
class Todo(Base):
    __tablename__ = "todos"
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    title = Column(
        String
    )
    completed = Column(
        Boolean,
        default=False
    )
# --------------------------------------------------
# 6. CREATE TABLES
# --------------------------------------------------
Base.metadata.create_all(bind=engine)
# --------------------------------------------------
# 7. DATABASE DEPENDENCY(DB session provide krega )
# --------------------------------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# --------------------------------------------------
# 8. FASTAPI APP
# --------------------------------------------------
app = FastAPI()
# --------------------------------------------------
# 9. ROUTE
# --------------------------------------------------
@app.get("/")
def home(db: Session = Depends(get_db)):

    return {
        "message": "DB Connected Fine"
    }

#  create api :
@app.post("/todos")
def create_todo(title:str,db:Session=Depends(get_db)):
    todo=Todo(title=title,completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "messages":"Todo Created ",
        "data":todo
    }

#  REad ALL DATA :
@app.get("/todos")
def get_data(db:Session =Depends(get_db)):
    todos=db.query(Todo).all()

    return{
        "message":"all data fetch",
        "Total":len(todos),
        "data":todos
    }

@app.get("/todoid/{todo_id}")
def get_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo_id:
        raise HTTPException(status_code=404,detail="Todo Not Found")

    return todo

#  Updating the Databases ::

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db :Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,detail="Todo Not Found")

    todo.title=title

    db.commit()
    db.refresh(todo)

    return{
        "messages":"TODO Updated ",
        "data":todo
    }

#  Deleting The Databases :
@app.delete("/todo/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,detail="Todo id Found")

    db.delete(todo)

    db.commit()

    return{
        "messages":"dlete succesfully",
        "data":todo
    }
