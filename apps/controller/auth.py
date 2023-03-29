from flasgger import Schema, SwaggerView, swag_from
from flask import Response, current_app, jsonify
from flask.blueprints import Blueprint

from apps.ultis.auth import jwt_encode, login_required

from ..docs.auth import post_login
from ..repository.user_repository import user_repo
from ..schemas.users import user_login_schema, users_schema
from ..ultis.decorator import parse_body
from ..ultis.error import Error, error_abort

auth_blueprint = Blueprint(
    name="auth", import_name=__name__, url_prefix="/auth"
)


@auth_blueprint.post("/login")
@swag_from(post_login)
@parse_body(model=user_login_schema)
def login(payload):
    user = user_repo.get_by_email(payload.get("email"))
    if not user:
        error_abort(Error.NOT_FOUND_EMAIL)
    token = jwt_encode(payload)
    return {"token": token}
