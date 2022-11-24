# register blue print here
from apps.user.controller.controller import user_blueprint


def register_blue_print(app):
    app.register_blueprint(user_blueprint)
