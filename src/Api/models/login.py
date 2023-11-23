from pydantic import BaseModel

class LoginBody(BaseModel):
  email: str
  password: str

class LoginResponse(BaseModel):
  access_token: str

class RegisterBody(BaseModel):
  email: str
  password: str
  username: str

class RegisterResponse(BaseModel):
  access_token: str