from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from ...utils.authentication import AuthenticationUtils
from ...services.user_service import UserService
from ...models.user import User, ShortUser
from os import environ as env
from jose import jwt