from src.usecase.task import TaskUsecases
from src.entity.task import Task

from fastapi import APIRouter, Depends

def task_api(usecase: TaskUsecases):
    
    def get_usecase():
        return usecase

    route = APIRouter(prefix="/t")

    @route.delete("/{task_id}")
    async def delete_task(task_id: int, usecase: TaskUsecases = Depends(get_usecase)):
        usecase.delete_task(task_id)
        return {"message": "Task deleted"}
    
    @route.post("/")
    async def add_task(task: Task, usecase: TaskUsecases = Depends(get_usecase)):
        new_task_id = usecase.add_task(task)
        return {"message": f"Task {new_task_id} added"}

    @route.get("/list")
    async def list_tasks(usecase: TaskUsecases = Depends(get_usecase)):
        return usecase.list_tasks()

    @route.get("/{task_id}")
    async def get_task(task_id: int, usecase: TaskUsecases = Depends(get_usecase)):
        return usecase.get_task(task_id)

    @route.post("/{task_id}")
    async def update_task(task_id: int, task: Task, usecase: TaskUsecases = Depends(get_usecase)):
        usecase.update_task(task_id, task)
        return {"message": f"Task {task_id} updated"}

    @route.post("/{task_id}/complete")
    async def complete_task(task_id: int, usecase: TaskUsecases = Depends(get_usecase)):
        usecase.complete_task(task_id)
        return {"message": f"Task {task_id} completed"}


    return route