from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user

from ...security.decorators import role_required

admin_analytics_bp = Blueprint("admin_analytics", __name__, url_prefix="/analytics")


@admin_analytics_bp.route("/")
@role_required("admin")
@login_required
def analytics():
    if current_user.role != "admin":
        abort(403)
    return render_template("admin/analytics.html")
