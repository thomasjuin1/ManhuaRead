from ..models.user import User, ShortUser
from typing import List
from json import load
from fastapi import HTTPException
from ..database.pymongo_manga_userdb import get_manga_user_by_id, get_all_manga_user, insert_manga_user, update_manga_user
from ..models.manga import Manga, MangaDb

class MangaUserService:

    @staticmethod
    async def get_is_reading():
        try:
            manga_list = get_all_manga()

            manga_list_db = []
            for manga in manga_list:
                manga_db : MangaDb = MangaDb()
                manga_db.manga_from_db(manga)
                manga_list_db.append(manga_db)
            return manga_list_db
        except Exception as e:
            raise Exception('Unable to load the asura mangas:', str(e))
        
    @staticmethod
    async def get_favorite(id: str):
        try:
            manga = get_manga_by_id(id)
            manga_db : MangaDb = MangaDb()
            manga_db.manga_from_db(manga)
            return manga_db
        except Exception as e:
            raise Exception('Unable to load the asura manga:', str(e))
        
    @staticmethod
    async def get_want_to_read(id: str):
        try:
            manga = get_manga_by_id(id)
            manga_db : MangaDb = MangaDb()
            manga_db.manga_from_db(manga)
            return manga_db
        except Exception as e:
            raise Exception('Unable to load the asura manga:', str(e))
        
    @staticmethod
    async def get_read(id: str):
        try:
            manga = get_manga_by_id(id)
            manga_db : MangaDb = MangaDb()
            manga_db.manga_from_db(manga)
            return manga_db
        except Exception as e:
            raise Exception('Unable to load the asura manga:', str(e))
