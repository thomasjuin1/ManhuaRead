from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from ..utils.authentication import AuthenticationUtils
from ..services.user_service import UserService
from ..services.manga_service import MangaService
from ..models.user import User, ShortUser
from ..models.manga import Manga
from os import environ as env
from jose import jwt

JWT_SECRET: str = ('JWT_SECRET')
router = APIRouter(prefix='/mangas')

@router.get('/')
def get_manga():
  try:
    return MangaService.get_manga_data()
  except:
    raise HTTPException(status_code=500, detail='Unable to load mangas data.')

@router.get('/{id}')
def get_manga_by_id(id: str):
  try:
    return MangaService.get_manga_by_id(id)
  except:
    raise HTTPException(status_code=500, detail='Unable to load manga data.')

@router.post('/start_polling')
def start_polling():
  try:
    return MangaService.start_polling()
  except:
    raise HTTPException(status_code=500, detail='Unable to start polling.')