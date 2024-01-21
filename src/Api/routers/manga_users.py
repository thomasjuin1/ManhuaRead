from fastapi import APIRouter, Depends, HTTPException, Header
from ..utils.authentication import AuthenticationUtils
from ..services.manga_user_service import MangaUserService
from ..models.user import User, ShortUser
from ..models.manga import Manga, MangaDb, MangaParams, MangaUserDb, MangaWithoutUser
from os import environ as env
from jose import jwt

JWT_SECRET: str = ('JWT_SECRET')
router = APIRouter(prefix='/manga_users', tags=['Manga Users'])

def format_manga_user(manga):
  manga_db : MangaUserDb = MangaUserDb()
  manga_db.format_from_db(manga)
  return manga_db

@router.get('/')
async def get_manga_user(extracted_id: str = Depends(AuthenticationUtils.extract_id)):
  try:
    mangas = await MangaUserService.get_all_mangas_user(extracted_id)
    return mangas
  except:
    raise HTTPException(status_code=500, detail='Unable to load mangas data.')

@router.get('/params')
async def get_manga_user(body: MangaParams, extracted_id: str = Depends(AuthenticationUtils.extract_id)):
  try:
    mangas = await MangaUserService.get_manga_by_param(extracted_id, body)
    return mangas
  except:
    raise HTTPException(status_code=500, detail='Unable to load mangas data.')
  
@router.post('/')
async def insert_manga_users(body: MangaWithoutUser, extracted_id: str = Depends(AuthenticationUtils.extract_id)):
  try:
    mangaParams = MangaParams(is_favorite=body.is_favorite, is_read=body.is_read, is_reading=body.is_reading, is_to_read=body.is_to_read, manga_chapter=body.manga_chapter)
    manga = await MangaUserService.update_manga_by_id(extracted_id, body.manga_id, mangaParams)
    manga = format_manga_user(manga)
    return manga
  except:
    raise HTTPException(status_code=500, detail='Unable to load manga data.')

@router.get('/new_chapter')
async def get_manga_user(extracted_id: str = Depends(AuthenticationUtils.extract_id)):
  try:
    mangas = await MangaUserService.get_new_mangas(extracted_id)
    return mangas
  except:
    raise HTTPException(status_code=500, detail='Unable to load mangas data.')