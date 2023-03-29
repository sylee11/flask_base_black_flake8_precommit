import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}".format(
        **{
            "USER": os.getenv("DB_USER", "root"),
            "PASSWORD": os.getenv("DB_PASSWORD", "root"),
            "HOST": os.getenv("DB_HOST", "localhost"),
            "PORT": os.getenv("DB_PORT", "3306"),
            "DB_NAME": os.getenv("DB_NAME", "matchdb"),
        }
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = os.getenv("SECRET_KEY", "123456")


class DevConfig(Config):
    pass


class StgConfig(Config):
    pass


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


env = os.getenv("ENV", "dev")
config = DevConfig
if env == "stg":
    config = StgConfig()
elif env == "prod":
    config = ProdConfig()
