from flasgger import swag_from
from flask import Response, current_app
from flask.blueprints import Blueprint

from ...ultis.error import error_abort
from ..repository.user_repository import user_repo
from ..schemas.users import users_schema

user_blueprint = Blueprint(
    name="user", import_name=__name__, url_prefix="/users"
)


@user_blueprint.get("")
@swag_from("../api_doc.yml")
def get_list():
    current_app.logger.info("TEST VO VO")
    user = user_repo.get_all()
    return users_schema.dump(user)
