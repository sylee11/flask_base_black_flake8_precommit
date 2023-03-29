from apps.schemas.users import users_schema
from apps.ultis.docs import error_401, error_403, error_500

get_all_user = {
    "security": [{"Bearer": []}],
    "responses": {
        # "200": users_schema.dump({}),
        "403": error_403,
        "401": error_401,
        "500": error_500,
    },
}
