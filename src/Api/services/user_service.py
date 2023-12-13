from ..models.user import User, ShortUser
from typing import List
from json import load
from fastapi import HTTPException
from ..database.pymongo_users import get_user_by_id, get_user_by_email, get_all_users, create_user, update_user, delete_user, get_user_login

class UserService:

  @staticmethod
  def format_shortuser(user) -> ShortUser:
    try:
      formated_user = ShortUser()
      formated_user.id = str(user['_id'])
      formated_user.email = user['email']
      formated_user.username = user['username']
      return formated_user
    except:
      raise Exception('Unable to format the user.')

  @staticmethod
  def format_user(user) -> User:
    try:
      formated_user = User()
      formated_user.email = user['email']
      formated_user.username = user['username']
      formated_user.is_superuser = user['is_superuser']
      return formated_user
    except:
      raise Exception('Unable to format the user.')

  @staticmethod
  def get_user_data(id: str) -> ShortUser:
    try:
      user = get_user_by_id(id)
      if (user == None):
        raise Exception('Unable to load the user.')
      return UserService.format_shortuser(user)
    except:
      raise Exception('Unable to load the user.')

  @staticmethod
  def get_user_by_email(email: str) -> User:
    try:
      user = get_user_by_email(email)
      new_user = UserService.format_user(user)
      return new_user
    except:
      raise Exception('Unable to load the user.')

  @staticmethod
  def get_login_user(body) -> User:
    try:
      user = get_user_login(body)
      return user
    except:
      raise Exception('Unable to load the user.')

  @staticmethod
  def register_user(user: User) -> User:
    try:
      new_user = create_user(user)
      return new_user
    except Exception as e:
      raise Exception(str(e))

  @staticmethod
  def get_users_data() -> List[ShortUser]:
    try:
      users = get_all_users()
      if (users == None):
        raise Exception('Unable to load the users.')
      formatted_users = []
      for user in users:
        formatted_users.append(UserService.format_shortuser(user))
      return formatted_users
    except:
      raise Exception('Unable to load the users.')
