from typing import Optional
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    name: str = Field(
        ..., title="Name of the task", max_length=64, example="Buy milk"
    )
    completed: Optional[bool]


class TaskCreate(TaskBase):
    pass


class TaskOut(TaskBase):
    id: int

    class Config:
        orm_mode = True


class Removed(BaseModel):
    removed: int = Field(
            ..., title="The ID of the removed element"
            )
