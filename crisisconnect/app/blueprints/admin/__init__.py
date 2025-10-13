from flask import Blueprint

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# Import and attach feature blueprints here
from .dashboard_routes import admin_dashboard_bp
from .alerts_routes import admin_alerts_bp
from .households_routes import admin_households_bp
from .kits_routes import admin_kits_bp
from .community_routes import admin_community_bp
from .reports_routes import admin_reports_bp
from .analytics_routes import admin_analytics_bp
from .system_routes import admin_system_bp

admin_bp.register_blueprint(admin_dashboard_bp)
admin_bp.register_blueprint(admin_alerts_bp)
admin_bp.register_blueprint(admin_households_bp)
admin_bp.register_blueprint(admin_kits_bp)
admin_bp.register_blueprint(admin_community_bp)
admin_bp.register_blueprint(admin_reports_bp)
admin_bp.register_blueprint(admin_analytics_bp)
admin_bp.register_blueprint(admin_system_bp)
