from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # Blueprints
    from routes.auth_routes import auth_bp
    from routes.dashboard_routes import dashboard_bp
    from routes.kit_routes import kit_bp
    from routes.household_routes import household_bp
    from routes.alert_routes import alert_bp
    from routes.community_routes import community_bp
    from routes.api_routes import api_bp
    from routes.main_routes import main_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(kit_bp)
    app.register_blueprint(household_bp)
    app.register_blueprint(alert_bp)
    app.register_blueprint(community_bp)
    app.register_blueprint(api_bp)

    return app
