from bson import ObjectId
from .pymongo_database import get_database
from ..models.user import User, ShortUser
from ..models.login import LoginBody
import logging

dbname = get_database()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_collection():
    try:
        collection_user = dbname["users"]
        return collection_user
    except Exception as e:
        raise Exception(str(e))

def get_user_by_id(id):
    try:
        logger.info("In database/pymongo_users.py/get_user_by_id()")
        collection_user = get_collection()
        value : ObjectId = ObjectId(id)
        user : User = collection_user.find_one({"_id": value})
        return user
    except Exception as e:
        raise Exception(str(e))

def get_user_by_email(mail):
    try:
        logger.info("In database/pymongo_users.py/get_user_by_email()")
        collection_user = get_collection()
        user = collection_user.find_one({"email": mail})
        return user
    except Exception as e:
        raise Exception(str(e))

def get_user_login(login: LoginBody):
    try:
        logger.info("In database/pymongo_users.py/get_user_login()")
        collection_user = get_collection()
        user = collection_user.find_one({"email": login.email, "password": login.password})
        if (user == None):
            raise Exception("User not found.")
        return user
    except Exception as e:
        raise Exception(str(e))

def get_all_users():
    try:
        logger.info("In database/pymongo_users.py/get_all_users()")
        collection_user = get_collection()
        user_cursor = collection_user.find()
        user_list = list(user_cursor)
        return user_list
    except Exception as e:
        raise Exception(str(e))

def create_user(user: User):
    try:
        logger.info("In database/pymongo_users.py/create_user()")
        collection_user = get_collection()
        if (collection_user.find_one({"email": user.email}) != None):
            raise Exception('Email already registered.')
        user_dict = user.dict()
        inserted_user = collection_user.insert_one(user_dict)
        user = collection_user.find_one({"_id": inserted_user.inserted_id})
        return user
    except Exception as e:
        raise Exception(str(e))

def update_user(id, user: User):
    try:
        logger.info("In database/pymongo_users.py/update_user()")
        collection_user = get_collection()
        user_dict = user.dict()
        user = collection_user.update_one({"_id": id}, {"$set": user_dict}, upsert=True)
    except Exception as e:
        raise Exception(str(e))

def delete_user(id):
    try:
        logger.info("In database/pymongo_users.py/delete_user()")
        collection_user = get_collection()
        collection_user.delete_one({"_id": id})
        return id
    except Exception as e:
        raise Exception(str(e))