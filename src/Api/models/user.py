from typing import Any
from pydantic import BaseModel
from .login import RegisterBody

class User(BaseModel):
    email: str = "email@gmail.com"
    password: str = "password"
    username: str = "username"
    is_superuser: bool = False

    def __init__(self):
        super().__init__()

    def __init__(self, RegisterBody : RegisterBody):
        super().__init__()
        self.email = RegisterBody.email
        self.password = RegisterBody.password
        self.username = RegisterBody.username

    def __str__(self):
        return "email: " + self.email + "\npassword: " + self.password + "\nusername: " + self.username + "\nis_superuser: " + str(self.is_superuser)
    
    def get(self):
        return self.email, self.password, self.username, self.is_superuser
    

class ShortUser(BaseModel):
    id: str = "1"
    email: str = "email@gmail.com"
    username: str = "username"

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "id: " + self.id + "\nemail: " + self.email + "\nusername: " + self.username

    def get(self):
        return self.id, self.email, self.username

