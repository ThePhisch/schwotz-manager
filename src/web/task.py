from src.entity.session import Session
from src.usecase.session import SessionUsecases
from src.usecase.task import TaskUsecases
from src.entity.task import Task

from fastapi import APIRouter, Depends, HTTPException, Request
from functools import wraps


def task_api(usecase: TaskUsecases, session_usecase: SessionUsecases):

    async def get_session(request: Request):
        """
        This is how we handle session in FastAPI

        We use the session_usecase to get the session from the request headers
        And we raise an HTTPException if the session is invalid
        Instead of using a decorator we use the Depends function to get the session
        """
        try:
            return session_usecase.get_session(request.headers.get("SCH-TOKEN", ""))
        except Exception as e:
            raise HTTPException(status_code=401, detail="Invalid session")

    def get_usecase():
        return usecase

    route = APIRouter(prefix="/t")

    @route.delete("/{task_id}")
    async def delete_task(
        task_id: int,
        usecase: TaskUsecases = Depends(get_usecase),
        session: Session = Depends(get_session),
    ):
        usecase.delete_task(task_id)
        return {"message": "Task deleted"}

    @route.post("/")
    async def add_task(
        task: Task,
        usecase: TaskUsecases = Depends(get_usecase),
        session: Session = Depends(get_session),
    ):
        new_task_id = usecase.add_task(task)
        return {"message": f"Task {new_task_id} added"}

    @route.get("/list")
    async def list_tasks(
        usecase: TaskUsecases = Depends(get_usecase),
        session: Session = Depends(get_session),
    ):
        return usecase.list_tasks()

    @route.get("/{task_id}")
    async def get_task(
        task_id: int,
        usecase: TaskUsecases = Depends(get_usecase),
        session: Session = Depends(get_session),
    ):
        return usecase.get_task(task_id)

    @route.post("/{task_id}")
    async def update_task(
        task_id: int,
        task: Task,
        usecase: TaskUsecases = Depends(get_usecase),
        session: Session = Depends(get_session),
    ):
        usecase.update_task(task_id, task)
        return {"message": f"Task {task_id} updated"}

    @route.post("/{task_id}/complete")
    async def complete_task(
        task_id: int,
        usecase: TaskUsecases = Depends(get_usecase),
        session: Session = Depends(get_session),
    ):
        usecase.complete_task(task_id)
        return {"message": f"Task {task_id} completed"}

    return route
