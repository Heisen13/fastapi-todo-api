from sqlalchemy.orm import Session
from models import ToDo
from schemas import ToDoCreate, ToDoUpdate

def get_tasks(db: Session):
    return db.query(ToDo).all()

def create_task(db: Session, task: ToDoCreate):
    db_task = ToDo(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: ToDoUpdate):
    db_task = db.query(ToDo).filter(ToDo.id == task_id).first()
    if db_task:
        db_task.title = task.title
        db_task.completed = task.completed
        db.commit()
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(ToDo).filter(ToDo.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()