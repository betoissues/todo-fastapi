from sqlalchemy.orm import Session
from app import models, schemas


def task_get_all(db: Session):
    return db.query(models.Task).all()

def task_get_by_id(db: Session, id: int):
    return db.query(models.Task).filter(models.Task.id == id).first()

def task_create(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(name=task.name)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
