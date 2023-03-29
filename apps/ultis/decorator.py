from functools import wraps

from flask import request
from marshmallow import ValidationError

from apps.ultis.error import Error, error_abort


def parse_body(model):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.json
            if not data:
                error_abort(Error(Error.JSON_PARSE_FAILED))

            try:
                result = model.load(data)
            except ValidationError as err:
                error_abort(Error(Error.VALIDATION_FAILED), err)

            return func(result, *args, **kwargs)

        return wrapper

    return decorator
