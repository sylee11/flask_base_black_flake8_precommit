import datetime
from functools import wraps

import jwt
from flask import request

from apps.ultis.date_time import get_time_exp, get_time_iat
from apps.ultis.error import Error, error_abort
from config import config


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            error_abort(Error(Error.UNAUTHORIZED))
        payload = decode_jwt(token)

        kwargs.update(payload)
        return func(*args, **kwargs)

    return wrapper


def jwt_encode(user_id: str):
    payload = {
        "iss": "token_iss",
        "sub": user_id,
        "aud": "token_aud",
        "exp": get_time_exp(),
        "iat": get_time_iat(),
    }
    return jwt.encode(payload, config.SECRET_KEY, algorithm="HS256")


def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(
            token,
            config.SECRET_KEY,
            issuer="token_iss",
            audience="token_aud",
            algorithms=["HS256"],
        )

    except jwt.exceptions.ExpiredSignatureError:
        error_abort(Error.TOKEN_EXPIRED)
        return

    except jwt.exceptions.InvalidTokenError:

        error_abort(Error.UNAUTHENTICATED)
        return

    except jwt.exceptions.InvalidSignatureError:
        error_abort(Error.UNAUTHENTICATED)
        return

    except Exception:
        error_abort(Error.UNAUTHENTICATED)
        return

    return decoded_token
