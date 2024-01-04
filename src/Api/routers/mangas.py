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
async def get_manga():
  try:
    mangas = await MangaService.get_manga_data()
    return mangas
  except:
    raise HTTPException(status_code=500, detail='Unable to load mangas data.')

@router.get('/{id}')
async def get_manga_by_id(id: str):
  try:
    manga = await MangaService.get_manga_by_id(id)
    return manga
  except:
    raise HTTPException(status_code=500, detail='Unable to load manga data.')
