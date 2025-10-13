from datetime import datetime
from flask import Flask
from flask_login import LoginManager
from .extensions import db, login_manager, migrate
from .config_loader import load_config
from .logging_config import setup_logging
from .models import User  # Import User for user_loader


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(load_config(config_name))
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    # Setup logging
    setup_logging(app)
    # Import models so Alembic sees them
    with app.app_context():
        from . import models  # Ensures Alembic detects all models

    # Register blueprints
    from .blueprints.auth import auth_bp
    from .blueprints.main import main_bp
    from .blueprints.user import user_bp
    from .blueprints.admin import admin_bp

    # from .api.v1 import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)

    # Configure Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.context_processor
    def inject_globals():
        return {"current_year": datetime.now().year, "app_version": "1.0.0"}

    return app
