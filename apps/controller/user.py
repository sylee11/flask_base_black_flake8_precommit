from flasgger import swag_from
from flask.blueprints import Blueprint

from apps.ultis.auth import login_required
from apps.ultis.response import return_paginate

from ..docs.user import get_all_user
from ..repository.user_repository import user_repo
from ..schemas.users import users_schema

user_blueprint = Blueprint(
    name="user", import_name=__name__, url_prefix="/users"
)


@user_blueprint.get("")
@login_required
@swag_from(get_all_user)
def get_list(**claims):
    users = user_repo.pagination(user_repo.filter(), 1, 20)
    return return_paginate(users, users_schema)
