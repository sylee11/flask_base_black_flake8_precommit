import os
from datetime import datetime, timedelta


def get_time_iat():
    return datetime.now().timestamp()


def get_time_exp():
    return (
        datetime.now()
        + timedelta(minutes=int(os.environ.get("JWT_MINUTES", 60)))
    ).timestamp()
