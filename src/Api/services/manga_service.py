from ..models.user import User, ShortUser
from typing import List
from json import load
from fastapi import HTTPException
from ..database.pymongo_users import get_user_by_id, get_user_by_email
from ..database.pymongo_manga import get_manga_by_id, get_all_manga, insert_manga, update_manga
from ..models.manga import Manga, MangaDb

class MangaService:

    @staticmethod
    async def get_manga_data():
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
    async def get_manga_by_id(id: str):
        try:
            print("Get manga by id")
            manga = get_manga_by_id(id)
            manga_db : MangaDb = MangaDb()
            manga_db.manga_from_db(manga)
            return manga_db
        except Exception as e:
            raise Exception('Unable to load the asura manga:', str(e))
