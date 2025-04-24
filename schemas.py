from pydantic import BaseModel

class ToDoCreate(BaseModel):
    title: str

class ToDoUpdate(BaseModel):
    title: str
    completed: bool

class ToDoOut(ToDoCreate):
    id: int
    completed: bool

    class Config:
        orm_mode = True