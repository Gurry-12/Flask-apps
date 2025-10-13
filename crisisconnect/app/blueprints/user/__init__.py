from flask import Blueprint

user_bp = Blueprint("user", __name__, url_prefix="/user")

# Import and attach feature blueprints here
from .dashboard_routes import user_dashboard_bp
from .alerts_routes import user_alerts_bp
from .households_routes import user_households_bp
from .kits_routes import user_kits_bp
from .community_routes import user_community_bp
from .profile_routes import user_profile_bp

user_bp.register_blueprint(user_dashboard_bp)
user_bp.register_blueprint(user_alerts_bp)
user_bp.register_blueprint(user_households_bp)
user_bp.register_blueprint(user_kits_bp)
user_bp.register_blueprint(user_community_bp)
user_bp.register_blueprint(user_profile_bp)
