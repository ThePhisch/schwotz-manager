from fastapi import Request, APIRouter, Depends
from pydantic import BaseModel
from src.usecase.session import SessionUsecases

class UPassData(BaseModel):
    username: str
    password: str

def session_api(usecase: SessionUsecases):
    def get_usecase(request: Request):
        return usecase

    route = APIRouter(prefix="/s")

    @route.post("/")
    async def new_session(
        upassdata: UPassData, usecase: SessionUsecases = Depends(get_usecase)
    ):
        try:
            token = usecase.new_session(upassdata.username, upassdata.password)
            return {"token": token}
        except ValueError as e:
            return {"error": str(e)}

    @route.delete("/{token}")
    async def close_session(
        token: str, usecase: SessionUsecases = Depends(get_usecase)
    ):
        usecase.close_session(token)
        return {"message": "Session closed"}

    @route.get("/{token}")
    async def get_session(
        token: str, usecase: SessionUsecases = Depends(get_usecase)
    ):
        try:
            return usecase.get_session(token)
        except ValueError as e:
            return {"error": str(e)}

    return route
