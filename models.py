from pydantic import BaseModel



class UserSingUp(BaseModel):
    login: str
    email: str
    password: str
    password_confirmation: str

class UserLogin(BaseModel):
    login: str
    password: str

class User(BaseModel):
    id: int = 0
    login: str = "joao"
    password: str = "123456"
    nome: str = "João Pé de Feijão"
    patrimonio: float = 1500
    gastos: float = 0
    ganhos: float = 0