from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
import models, crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos", response_model=list[schemas.ToDoOut])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.post("/todos", response_model=schemas.ToDoOut)
def create_task(task: schemas.ToDoCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.put("/todos/{task_id}", response_model=schemas.ToDoOut)
def update_task(task_id: int, task: schemas.ToDoUpdate, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task)

@app.delete("/todos/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    crud.delete_task(db, task_id)
    return {"message": "Task deleted"}