from bson import ObjectId
from .pymongo_database import get_database
from ..models.user import User, ShortUser
from ..models.manga import Manga
from ..models.login import LoginBody
import logging

from src.Api.models import manga

dbname = get_database()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_collection():
    try:
        collection_manga = dbname["manga"]
        return collection_manga
    except Exception as e:
        raise Exception(str(e))

def get_manga_by_id(id):
    try:
        collection_manga = get_collection()
        objId : ObjectId = ObjectId(id)
        manga = collection_manga.find_one({"_id": objId})
        if not manga:
            logger.warning("No manga found on id : "+ id)
        return manga
    except Exception as e:
        raise Exception(str(e))

def get_all_manga():
    try:
        logger.info("In database/pymongo_manga.py/get_all_manga()")
        collection_manga = get_collection()
        manga_cursor = collection_manga.find()
        manga_list = list(manga_cursor) # This is where the error is
        if not manga_list:
            logger.warning("No mangas found.")
        return manga_list
    except Exception as e:
        raise Exception(str(e))

def insert_manga(manga: Manga):
    try:
        collection_manga = get_collection()
        manga_dict = manga.dict()
        inserted_manga = collection_manga.insert_one(manga_dict)
        manga = collection_manga.find_one({"_id": inserted_manga.inserted_id})
        return manga
    except Exception as e:
        raise Exception(str(e))

def update_manga(manga: Manga):
    try:
        collection_manga = get_collection()
        manga_dict = manga.dict()
        collection_manga.update_one({"title": manga.title}, {"$set": manga_dict}, upsert=True)
        manga = collection_manga.find_one({"title": manga.title})
        return manga
    except Exception as e:
        raise Exception(str(e))
