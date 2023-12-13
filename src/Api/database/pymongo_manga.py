from .pymongo_database import get_database
from ..models.user import User, ShortUser
from ..models.manga import Manga
from ..models.login import LoginBody
import logging

dbname = get_database()

def get_collection():
    try:
        collection_manga = dbname["manga"]
        return collection_manga
    except Exception as e:
        raise Exception(str(e))

def get_manga_by_id(id):
    try:
        collection_manga = get_collection()
        value : int = int(id)
        manga : Manga = collection_manga.find_one({"_id": value})
        return manga
    except Exception as e:
        raise Exception(str(e))

def get_all_manga():
    try:
        collection_manga = get_collection()
        manga_cursor = collection_manga.find()
        manga_list = list(manga_cursor)
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
        collection_manga.update_one({"_id": manga.id}, {"$set": manga_dict})
        manga = collection_manga.find_one({"_id": manga.id})
        return manga
    except Exception as e:
        raise Exception(str(e))
