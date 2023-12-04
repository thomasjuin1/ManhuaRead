from pydantic import BaseModel
from ...Asura.manga_class import Manga

# class Manga(BaseModel):
#    self.title = None
#    self.type = None
#    self.status = None
#    self.chapters = None
#    self.note = None
#    self.link = None
#    self.image = None
#    self.synopsis = None
#    self.genres = None

class MangaDb(BaseModel):

    def __init__(self, manga : Manga):
        self.manga : Manga = manga

    def __str__(self):
        value = ""
        for (key, val) in self.__dict__.items():
            if (val):
                value = value + key + ": "+str(val)+"\n"
        return value

class MangaUserDb(BaseModel):

    def __init__(self):
        self.manga_id = None
        self.is_favorite : bool = False
        self.is_read : bool = False
        self.is_reading : bool = False
        self.is_to_read : bool = False

    def __str__(self):
        value = ""
        for (key, val) in self.__dict__.items():
            if (val):
                value = value + key + ": "+str(val)+"\n"
        return value


