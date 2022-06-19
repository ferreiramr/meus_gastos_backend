from pydantic import BaseModel


class UserSingUp(BaseModel):
    login: str
    email: str
    password: str
    password_confirmation: str