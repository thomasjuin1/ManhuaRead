from fastapi import Request
from jose import jwt
from os import environ as env

JWT_SECRET: str = ('JWT_SECRET')

class AuthenticationUtils:
  @staticmethod
  def extract_id(req: Request) -> int:
    authorization = req.headers.get('authorization', None)

    print(authorization)
    if authorization is None:
      return None

    try:
      bearer = authorization.split(' ')[1]
      decoded = jwt.decode(bearer, JWT_SECRET, algorithms=['HS256'])

      return decoded.get('id')
    except:
      return None