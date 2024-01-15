from bson import ObjectId
from .pymongo_database import get_database
from ..models.manga import MangaUserDb, MangaParams
import logging

dbname = get_database()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_collection():
    try:
        collection_manga = dbname["manga_users"]
        return collection_manga
    except Exception as e:
        raise Exception(str(e))

def get_all_manga_user(id_user):
    try:
        logger.info("In database/pymongo_manga.py/get_all_manga_user()")
        collection_manga = get_collection()
        manga_cursor = collection_manga.find({"id_user": id_user})
        manga_list = list(manga_cursor)
        if not manga_list:
            logger.warning("No mangas found.")
        return manga_list
    except Exception as e:
        raise Exception(str(e))
    
def get_manga_by_parameters(id_user, params: MangaParams):
    try:
        logger.info("In database/pymongo_manga.py/get_manga_by_parameters()")
        collection_manga = get_collection()
        manga_cursor = collection_manga.find({"id_user": id_user, "is_reading": params.is_reading, "is_favorite": params.is_favorite, "is_to_read": params.is_to_read, "is_read": params.is_read})
        manga_list = list(manga_cursor)
        if not manga_list:
            logger.warning("No mangas found.")
        return manga_list
    
    except Exception as e:
        raise Exception(str(e))

def get_manga_user_by_id(id):
    try:
        logger.info("In database/pymongo_manga.py/get_manga_by_id()")
        collection_manga = get_collection()
        objId : ObjectId = ObjectId(id)
        manga = collection_manga.find_one({"_id": objId})
        if not manga:
            logger.warning("No manga found on id : "+ id)
        return manga
    except Exception as e:
        raise Exception(str(e))
    
def insert_manga_user(manga: MangaUserDb):
    try:
        logger.info("In database/pymongo_manga.py/insert_manga()")
        collection_manga = get_collection()
        manga_dict = manga.dict()
        inserted_manga = collection_manga.insert_one(manga_dict)
        manga = collection_manga.find_one({"_id": inserted_manga.inserted_id})
        return manga
    except Exception as e:
        raise Exception(str(e))
    
def update_manga_user(manga: MangaUserDb):
    try:
        logger.info("In database/pymongo_manga.py/update_manga()")
        collection_manga = get_collection()
        manga_dict = manga.dict()
        collection_manga.update_one({"title": manga.title}, {"$set": manga_dict}, upsert=True)
        manga = collection_manga.find_one({"title": manga.title})
        return manga
    except Exception as e:
        raise Exception(str(e))

def delete_manga_user(id):
    try:
        logger.info("In database/pymongo_manga.py/delete_manga()")
        collection_manga = get_collection()
        objId : ObjectId = ObjectId(id)
        collection_manga.delete_one({"_id": objId})
    except Exception as e:
        raise Exception(str(e))

def delete_all_manga_user(id_user):
    try:
        logger.info("In database/pymongo_manga.py/delete_all_manga_user()")
        collection_manga = get_collection()
        collection_manga.delete_many({"id_user": id_user})
    except Exception as e:
        raise Exception(str(e))