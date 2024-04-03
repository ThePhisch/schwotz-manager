from typing import Annotated

from fastapi import FastAPI, Depends

from src.usecase.task import TaskUsecases


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

    return app