from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from ...models import User, Alert, Household, Kit, Community
from ...security.decorators import role_required

admin_dashboard_bp = Blueprint("admin_dashboard", __name__, url_prefix="/dashboard")


@admin_dashboard_bp.route("/")
@role_required("admin")
@login_required
def index():
    if not hasattr(current_user, "role") or current_user.role != "admin":
        abort(403)
    users = User.query.all()
    alerts = Alert.query.all()
    households = Household.query.all()
    kits = Kit.query.all()
    communities = Community.query.all()
    return render_template(
        "admin/dashboard.html",
        users=users,
        alerts=alerts,
        households=households,
        kits=kits,
        communities=communities,
    )
