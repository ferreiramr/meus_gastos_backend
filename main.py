from fastapi import FastAPI
from fastapi import status
from fastapi.responses import JSONResponse

from models import UserSingUp

app = FastAPI()

@app.post("/login", )
async def login(user: UserSingUp):
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "action": "Create User",
            "result": "User Created",
            "status_code": status.HTTP_201_CREATED
        }
    )