from fastapi import APIRouter, Depends, Request
from src.entity.user import User
from src.usecase.user import UserUsecases


def user_api(usecase: UserUsecases):

    def get_usecase(request: Request):
        return usecase

    route = APIRouter(prefix="/u")

    @route.delete("/{user_id}")
    async def delete_user(user_id: int, usecase: UserUsecases = Depends(get_usecase)):
        usecase.delete_user(user_id)
        return {"message": "User deleted"}

    @route.post("/")
    async def add_user(user: User, usecase: UserUsecases = Depends(get_usecase)):
        new_user_id = usecase.add_user(user)
        return {"message": f"User {new_user_id} added"}

    @route.get("/list")
    async def list_users(usecase: UserUsecases = Depends(get_usecase)):
        return usecase.list_users()

    @route.get("/{user_id}")
    async def get_user(user_id: int, usecase: UserUsecases = Depends(get_usecase)):
        return usecase.get_user(user_id)

    @route.post("/{user_id}")
    async def update_user(user_id: int, task: User, usecase: UserUsecases = Depends(get_usecase)):
        usecase.update_user(user_id, task)
        return {"message": f"User {user_id} updated"}

    return route 

