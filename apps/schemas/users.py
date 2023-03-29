"""
please import models to ./migrations/env.py to Flask Migrate working
"""
from extensions.database import ma

from ..models.users import Users


class UserSchema(ma.Schema):
    class Meta:
        model = Users
        fields = ("id", "email", "company_name", "_links")

    _links = "sss"


class UserLoginSchema(ma.Schema):
    class Meta:
        model = Users
        fields = ("email",)


user_schema = UserSchema()
user_login_schema = UserLoginSchema()
users_schema = UserSchema(many=True)
