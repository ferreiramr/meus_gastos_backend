from fastapi.exceptions import HTTPException
from fastapi import FastAPI
from fastapi import status
from fastapi.responses import JSONResponse

from models import User, UserSingUp, UserLogin

app = FastAPI()
joao = User()
usuarios = [joao]


@app.post("/singin")
async def singin(user: UserSingUp):
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "action": "Create User",
            "result": "User Created",
            "status_code": status.HTTP_201_CREATED
        }
    )

@app.post("/login")
async def login(user: UserLogin):
    #for na liste de usuarios para ver se ele existe, se tiver certo loga, se naõ retorna erro
    for usuario in usuarios:
        if usuario.login == user.login:
            if usuario.password != user.password:
                raise HTTPException(
                    status_code = status.HTTP_401_UNAUTHORIZED,
                    detail="Usuário ou senha incorretos"
                )
            return usuario
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Usuário ou senha incorretos"
    )
    

# @app.post("/patrimonio")
# async def getUser(user: User):
#     return JSONResponse(
#         status_code=status.HTTP_200_OK,
#         content={
#             "message": "Usuário logado"
#         }
#     )

@app.get("/usuario/{id}")
async def getUsuario(id: int):
    usuario = usuarios[id]
    return usuario

@app.get("/add_gastos/{id}")
async def add_gastos(gasto: float, id: int):
    usuario = usuarios[id]
    usuario.gastos += gasto
    usuario.patrimonio -= gasto
    return usuario

@app.get("/add_ganhos/{id}")
async def add_ganhos(ganhos: float, id: int):
    usuario = usuarios[id]
    usuario.ganhos += ganhos
    usuario.patrimonio += ganhos
    return usuario

@app.post("/create_user")
async def create_user(usuario: User):
    usuario.id = len(usuarios) - 1
    usuarios.append(usuario)
    return usuario

@app.get("/users")
async def get_users():
    return usuarios