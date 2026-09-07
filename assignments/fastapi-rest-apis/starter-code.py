from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


# Keep data in memory while the API is running.
tasks: list[Task] = []


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return tasks


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):
    next_id = len(tasks) + 1
    task = Task(id=next_id, **task_data.model_dump())
    tasks.append(task)
    return task


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, completed: bool):
    for task in tasks:
        if task.id == task_id:
            task.completed = completed
            return task

    return {"detail": "Task not found"}
