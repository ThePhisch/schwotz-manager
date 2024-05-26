from fastapi import HTTPException, Request, APIRouter, Depends
from pydantic import BaseModel
from src.usecase.session import SessionUsecases
from src.entity.session import Session

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
        # TODO: make sure that new session is not created if there is already a session
        try:
            token = usecase.new_session(upassdata.username, upassdata.password)
            return {"token": token}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))

    @route.delete("/{token}")
    async def close_session(
        token: str, usecase: SessionUsecases = Depends(get_usecase)
    ):
        usecase.close_session(token)
        return {"message": "Session closed"}

    @route.get("/{token}")
    async def get_session(
        token: str, usecase: SessionUsecases = Depends(get_usecase)
    ) -> Session:
        try:
            return usecase.get_session(token)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return route
