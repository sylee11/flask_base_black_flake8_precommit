import typing
from enum import IntEnum, auto
from http import HTTPStatus

from flask import abort


# noinspection PyArgumentList
class Error(IntEnum):
    def __new__(cls, value: int, status_code: int, reason: str = None):
        obj = int.__new__(cls)
        obj._value_ = value

        obj.status_code = status_code
        obj.reason = reason
        return obj

    @classmethod
    def members_as_list(cls):
        return [*cls.__members__.values()]

    # BAD_REQUEST (400)
    JSON_PARSE_FAILED = (
        auto(),
        HTTPStatus.BAD_REQUEST.value,
        "jsonParseFailed",
    )
    VALIDATION_FAILED = (
        auto(),
        HTTPStatus.BAD_REQUEST.value,
        "validationFailed",
    )
    UNAUTHORIZED = (
        auto(),
        HTTPStatus.UNAUTHORIZED.value,
        "UnauthorizedFail",
    )
    NOT_FOUND_EMAIL = (
        auto(),
        HTTPStatus.NOT_FOUND.value,
        "NotFoundDeal",
    )

    UNAUTHENTICATED = (
        auto(),
        HTTPStatus.UNAUTHORIZED.value,
        "UnAuthenticated",
    )

    TOKEN_EXPIRED = (
        auto(),
        HTTPStatus.UNAUTHORIZED.value,
        "TokenExpired",
    )


def error_abort(error_type: Error, errors: typing.List = None):
    for c in Error.members_as_list():
        if error_type.value == c.value:
            if errors:
                abort(c.status_code, errors)
            else:
                abort(c.status_code)


class NotFound(Exception):
    pass


class Conflict(Exception):
    pass


class Unauthorized(Exception):
    pass


class Forbidden(Exception):
    pass
