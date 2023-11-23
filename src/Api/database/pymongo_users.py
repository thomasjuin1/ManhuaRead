from .pymongo_database import get_database
from ..models.user import User, ShortUser
from ..models.login import LoginBody
import logging


dbname = get_database()

def get_collection():
    try:
        collection_user = dbname["users"]
        return collection_user
    except:
        return None

def get_user_by_id(id):
    try:
        collection_user = get_collection()
        value : int = int(id)
        user : User = collection_user.find_one({"_id": value})
        return user
    except:
        return None

def get_user_by_email(mail):
    try:
        collection_user = get_collection()
        user = collection_user.find_one({"email": mail})
        return user
    except:
        return None

def get_user_login(login: LoginBody):
    try:
        collection_user = get_collection()
        user = collection_user.find_one({"email": login.email, "password": login.password})
        return user
    except:
        return None

def get_all_users():
    try:
        collection_user = get_collection()
        user_cursor = collection_user.find()
        user_list = list(user_cursor)
        return user_list
    except:
        return None

def create_user(user: User):
    try:
        collection_user = get_collection()
        user_dict = user.dict()
        inserted_user = collection_user.insert_one(user_dict)
        return inserted_user
    except:
        return None

def update_user(id, user: User):
    try:
        collection_user = get_collection()
        user = collection_user.update_one({"_id": id}, {"$set": user.model_dump(by_alias=True)})
    except:
        return None

def delete_user(id):
    try:
        collection_user = get_collection()
        collection_user.delete_one({"_id": id})
        return id
    except:
        return None