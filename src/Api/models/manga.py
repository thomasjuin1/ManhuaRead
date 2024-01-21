import re
from pydantic import BaseModel

from src.Api.models import user
from ...Asura.manga_class import Manga

class Manga(BaseModel):
    title : str = None
    type : str = None
    status : str = None
    chapters : str = None
    note : str = None
    link : str = None
    image : str = None
    synopsis : str = None
    genres : list = None

    def __init__(self):
        super().__init__()
        self.title = None
        self.type = None
        self.status = None
        self.chapters = None
        self.note = None
        self.link = None
        self.image = None
        self.synopsis = None
        self.genres = None

    def __str__(self):
        value = ""
        for (key, val) in self.__dict__.items():
            if (val.__class__ == list):
                value = value + key + ": "
                for genre in val:
                    value = value + genre
                    if (genre != val[-1]):
                        value = value + ", "
                continue
            if (val):
                value = value + key + ": "+str(val)+"\n"
        return value

class MangaDb(BaseModel):
    title : str = None
    type : str = None
    status : str = None
    chapters : str = None
    note : str = None
    link : str = None
    image : str = None
    synopsis : str = None
    genres : list = None
    id : str = None

    def __str__(self):
        value = ""
        for (key, val) in self.__dict__.items():
            if (val):
                value = value + key + ": "+str(val)+"\n"
        return value

    def to_manga(self):
        manga : Manga = Manga()
        manga.title = self.title
        manga.type = self.type
        manga.status = self.status
        manga.chapters = self.chapters
        manga.note = self.note
        manga.link = self.link
        manga.image = self.image
        manga.synopsis = self.synopsis
        manga.genres = self.genres
        return manga

    def manga_from_db(self, manga):
        self.id = str(manga["_id"])
        self.title = manga["title"]
        self.type = manga["type"]
        self.status = manga["status"]
        self.chapters = manga["chapters"]
        self.note = manga["note"]
        self.link = manga["link"]
        self.image = manga["image"]
        self.synopsis = manga["synopsis"]
        self.genres = manga["genres"]
        return self
    
class MangaUserDb(BaseModel):
    user_id : str = None
    manga_id : str = None
    manga_chapter : int = 0
    is_favorite : bool = False
    is_read : bool = False
    is_reading : bool = False
    is_to_read : bool = False

    def __str__(self):
        value = ""
        for (key, val) in self.__dict__.items():
            if (val):
                value = value + key + ": "+str(val)+"\n"
        return value

    def __init__(self):
        super().__init__()
        self.user_id = None
        self.manga_id = None
        self.manga_chapter = 0
        self.is_favorite = False
        self.is_read = False
        self.is_reading = False
        self.is_to_read = False
        
    def format_from_db(self, manga):
        self.user_id = manga["user_id"]
        self.manga_id = manga["manga_id"]
        self.manga_chapter = manga["manga_chapter"]
        self.is_favorite = manga["is_favorite"]
        self.is_read = manga["is_read"]
        self.is_reading = manga["is_reading"]
        self.is_to_read = manga["is_to_read"]
        return self

class MangaWithoutUser(BaseModel):
    manga_id : str = None
    manga_chapter : int = 0
    is_favorite : bool = False
    is_read : bool = False
    is_reading : bool = False
    is_to_read : bool = False
    
    def __str__(self):
        value = ""
        for (key, val) in self.__dict__.items():
            if (val):
                value = value + key + ": "+str(val)+"\n"
        return value

class MangaParams(BaseModel):
    manga_chapter : int = 0
    is_favorite : bool = False
    is_read : bool = False
    is_reading : bool = False
    is_to_read : bool = False

    def __str__(self):
        value = ""
        for (key, val) in self.__dict__.items():
            if (val):
                value = value + key + ": "+str(val)+"\n"
        return value