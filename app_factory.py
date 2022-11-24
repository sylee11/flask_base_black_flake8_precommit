import json
import traceback
from http import HTTPStatus

from flask import Flask, current_app, request
from flask_cors import CORS

from apps.ultis.error import Conflict, Forbidden, Unauthorized
from config import config
from extensions.blueprint import register_blue_print
from extensions.database import db, ma, migrate, swagger
from extensions.logging import get_logger

app = Flask(__name__)


def create_app():
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    swagger.init_app(app)
    CORS(app)
    register_blue_print(app)

    # @app.before_request
    # def before_request():
    #     if request.content_type == 'application/json':
    #         request_body = json.dumps(request.json, indent=2, ensure_ascii=False) \
    #             if hasattr(request, 'json') else None
    #
    #         app.logger.debug(
    #             "\n===========\nrequest\n==========="
    #             f"\nurl: {request.method} {request.url}"
    #             f"\n{request.headers}"
    #             f"body: {request_body}")

    # @app.after_request
    # def after_request(response):
    #     response_body = json.dumps(response.json, indent=2, ensure_ascii=False) if response.json else None
    #
    #     app.logger.debug(
    #         "\n\n===========\nresponse\n==========="
    #         f"\nstatus: {response.status}"
    #         f"\n{response.headers}"
    #         f"\nbody: {response_body}")
    #     return response

    @app.errorhandler(Exception)
    def error_handler(ex):
        app.logger.error(traceback.format_exc())
        return {
            "message": HTTPStatus.INTERNAL_SERVER_ERROR.name
        }, HTTPStatus.INTERNAL_SERVER_ERROR.value

    @app.errorhandler(Conflict)
    def conflict_handler(error):
        return {
            "message": HTTPStatus.CONFLICT.description
        }, HTTPStatus.CONFLICT.value

    @app.errorhandler(Unauthorized)
    def unauthorized_handler(error):
        return {
            "message": HTTPStatus.UNAUTHORIZED.description
        }, HTTPStatus.UNAUTHORIZED.value

    @app.errorhandler(Forbidden)
    def forbidden_handler(error):
        return {
            "message": HTTPStatus.FORBIDDEN.description
        }, HTTPStatus.FORBIDDEN.value

    return app
