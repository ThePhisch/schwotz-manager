from typing import Annotated

from fastapi import FastAPI, Depends

from src.usecase.task import TaskUsecases
from src.entity.task import Task


def create_app(usecase: TaskUsecases):
    
    def get_usecase():
        return usecase

    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.get("/db")
    async def db(usecase: TaskUsecases = Depends(get_usecase)):
        return usecase.list_tasks()

    @app.delete("/t/{task_id}")
    async def delete_task(task_id: int, usecase: TaskUsecases = Depends(get_usecase)):
        usecase.delete_task(task_id)
        return {"message": "Task deleted"}
    
    @app.post("/t")
    async def add_task(task: Task, usecase: TaskUsecases = Depends(get_usecase)):
        new_task_id = usecase.add_task(task)
        return {"message": f"Task {new_task_id} added"}

    @app.get("/t/list")
    async def list_tasks(usecase: TaskUsecases = Depends(get_usecase)):
        return usecase.list_tasks()

    @app.get("/t/{task_id}")
    async def get_task(task_id: int, usecase: TaskUsecases = Depends(get_usecase)):
        return usecase.get_task(task_id)

    @app.post("/t/{task_id}")
    async def update_task(task_id: int, task: Task, usecase: TaskUsecases = Depends(get_usecase)):
        usecase.update_task(task_id, task)
        return {"message": f"Task {task_id} updated"}

    @app.post("/t/{task_id}/complete")
    async def complete_task(task_id: int, usecase: TaskUsecases = Depends(get_usecase)):
        usecase.complete_task(task_id)
        return {"message": f"Task {task_id} completed"}


    return app