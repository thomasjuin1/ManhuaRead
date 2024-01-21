from hmac import new
from ..models.user import User, ShortUser
from typing import List
from json import load
from fastapi import HTTPException
from ..database.pymongo_manga_userdb import get_manga_by_parameters, get_all_manga_user, insert_manga_user, get_manga_user_by_id_manga, update_manga_user
from ..database.pymongo_manga import get_manga_by_id
from ..models.manga import Manga, MangaDb, MangaParams, MangaUserDb, MangaWithoutUser

class MangaUserService:

    @staticmethod
    async def get_manga_by_param(id_user, manga_params):

        def format_manga_user(manga):
            manga_db : MangaUserDb = MangaUserDb()
            manga_db.format_from_db(manga)
            return manga_db

        try:
            manga_list = get_manga_by_parameters(id_user, manga_params)

            manga_list_db = []
            for manga in manga_list:
                manga_db : MangaUserDb = format_manga_user(manga)
                manga_list_db.append(manga_db)
            return manga_list_db
        except Exception as e:
            raise Exception('Unable to load the asura manga:', str(e))

    @staticmethod
    async def update_manga_by_id(id_user, id_manga, manga_params : MangaParams):
        try:
            manga : MangaUserDb = get_manga_user_by_id_manga(id_manga, id_user)
            if (manga == None):
                manga : MangaUserDb = MangaUserDb()
                manga.user_id = id_user
                manga.manga_id = id_manga
                manga.is_reading = manga_params.is_reading
                manga.is_favorite = manga_params.is_favorite
                manga.is_to_read = manga_params.is_to_read
                manga.is_read = manga_params.is_read
                manga.manga_chapter = manga_params.manga_chapter
            else:
                manga.is_reading = manga_params.is_reading
                manga.is_favorite = manga_params.is_favorite
                manga.is_to_read = manga_params.is_to_read
                manga.is_read = manga_params.is_read
                manga.manga_chapter = manga_params.manga_chapter
            manga = update_manga_user(manga)
            return manga
        except Exception as e:
            raise Exception('Unable to load the asura manga:', str(e))
        
    @staticmethod
    async def get_all_mangas_user(id_user):

        def format_manga_user(manga):
            manga_db : MangaUserDb = MangaUserDb()
            manga_db.format_from_db(manga)
            return manga_db

        try:
            manga_list = get_all_manga_user(id_user)
            manga_list_db = []
            
            for manga in manga_list:
                manga_db : MangaUserDb = format_manga_user(manga)
                manga_list_db.append(manga_db)
            return manga_list_db
        except Exception as e:
            raise Exception('Unable to load the asura manga:', str(e))
        
    @staticmethod
    async def get_new_mangas(id_user):

        def format_manga_user(manga):
            manga_db : MangaUserDb = MangaUserDb()
            manga_db.format_from_db(manga)
            return manga_db

        try:
            manga_list = get_all_manga_user(id_user)
            manga_list_db = []
            new_manga_list = []
            for manga in manga_list:
                manga_db : MangaUserDb = format_manga_user(manga)
                manga_list_db.append(manga_db)
            for manga in manga_list_db:
                manga_db : MangaDb = get_manga_by_id(manga.manga_id)
                if (manga_db == None):
                    pass
                new_manga : MangaDb = MangaDb()
                new_manga.manga_from_db(manga_db)

                if (int(new_manga.chapters) > int(manga.manga_chapter)):
                    new_manga_list.append(new_manga)
            return new_manga_list
        except Exception as e:
            raise Exception('Unable to load the asura manga:', str(e))