from typing import Annotated

from fastapi import APIRouter, FastAPI, Depends

def core_api():
    route = APIRouter(prefix="")

    @route.get("/")
    async def root():
        return {"message": "Hello World"}
    return route

def create_app(routes: list[APIRouter]):
    app = FastAPI()
    for r in routes:
        # TODO: add logging
        app.include_router(r)
    return app
