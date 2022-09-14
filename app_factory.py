from flask import Flask, current_app
from flask_cors import CORS
from flask_migrate import Migrate

from config import config
from extensions.database import db, migrate
from extensions.logging import get_logger

app = Flask(__name__)


def create_app():
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    return app
