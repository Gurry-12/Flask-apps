import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev_secret_key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True

    # Ensure instance directory exists
    instance_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "instance")
    os.makedirs(instance_dir, exist_ok=True)

    # SQLite database path (Windows-safe)
    db_path = os.path.join(instance_dir, "crisis_connect.db").replace("\\", "/")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


def get_config(env="development"):
    configs = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig,
    }
    return configs.get(env, DevelopmentConfig)
