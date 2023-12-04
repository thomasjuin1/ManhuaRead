from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from ..utils.authentication import AuthenticationUtils
from ..services.user_service import UserService
from ..models.login import LoginBody, LoginResponse, RegisterBody, RegisterResponse
from ..models.user import User
from os import environ as env
from jose import jwt

JWT_SECRET: str = ('JWT_SECRET')
router = APIRouter(prefix='/users')

@router.post('/login')
def login(body: LoginBody) -> LoginResponse:
  try:
    user = UserService.get_login_user(body)
    new_user = UserService.format_shortuser(user)
    return LoginResponse(
      access_token=jwt.encode(dict(new_user), JWT_SECRET, algorithm='HS256')
    )
  except Exception as e:
    print(e)
    raise HTTPException(status_code=404, detail='User not found.')

@router.post('/register')
def register(body: RegisterBody) -> RegisterResponse:
  try:
    user : User = User(body)
    user = UserService.register_user(user)
    new_user = UserService.format_shortuser(user)
    return RegisterResponse(
      access_token=jwt.encode(dict(new_user), JWT_SECRET, algorithm='HS256')
    )
  except (Exception) as error:
    print(error)
    raise HTTPException(status_code=500, detail='Unable to register the user.')

@router.get('/')
def get_user():
  try:
    return UserService.get_users_data()
  except:
    raise HTTPException(status_code=500, detail='Unable to load users data.')
