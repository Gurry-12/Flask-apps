import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging(app):
    if not os.path.exists("logs"):
        os.makedirs("logs")
    # General app log
    file_handler = RotatingFileHandler("logs/app.log", maxBytes=10240, backupCount=10)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        )
    )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    # Error log
    error_handler = RotatingFileHandler(
        "logs/error.log", maxBytes=10240, backupCount=10
    )
    error_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        )
    )
    error_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info("CrisisConnect startup")
