# register blue print here
from apps.controller.auth import auth_blueprint
from apps.controller.user import user_blueprint


def register_blue_print(app):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)
