from pydantic import BaseModel
from .login import RegisterBody

class User(BaseModel):
    email: str = "email@gmail.com"
    password: str = "password"
    username: str = "username"
    is_superuser: bool = False

    def __init__(self, RegisterBody : RegisterBody):
        super().__init__()
        self.email = RegisterBody.email
        self.password = RegisterBody.password
        self.username = RegisterBody.username


class ShortUser(BaseModel):
    id: str = "1"
    email: str = "email@gmail.com"
    username: str = "username"

    def __init__(self):
        super().__init__()

