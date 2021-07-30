from hashlib import algorithms_guaranteed
import time
from typing import Dict

from jose import JWTError, jwt
from decouple import config


def token_response(token: str):
    return {
        "code": 200,
        "access_token": token
    }


SECRET_KEY = config('secret')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def signJWT(user_email: str) -> Dict[str, str]:
    # Set the expiry time.
    payload = {
        'user_email': user_email,
        'expires': time.time() + (ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    }
    return token_response(jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM))


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token.encode(), SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token if decoded_token['expires'] >= time.time() else None
    except:
        return {}
