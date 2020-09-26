from app import crud, schemas
from app.db import get_db
from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()


@router.get("/tasks", response_model=List[schemas.TaskOut])
async def read_tasks(db: Session = Depends(get_db)):
    return crud.task_get_all(db)


@router.post("/tasks",
             response_model=schemas.TaskOut,
             status_code=status.HTTP_201_CREATED)
async def add_task(task: schemas.TaskCreate,
                   db: Session = Depends(get_db)):
    return crud.task_create(db=db, task=task)


@router.get("/tasks/{task_id}", response_model=schemas.TaskOut)
async def read_task(
        task_id: int = Path(..., title="The ID of the Task"),
        db: Session = Depends(get_db)):
    task = crud.task_get_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/tasks/{task_id}", response_model=schemas.Removed)
async def read_task(
        task_id: int = Path(..., title="The ID of the Task"),
        db: Session = Depends(get_db)):
    task = crud.task_get_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.task_delete(db, task)
    return {'removed': task_id}
