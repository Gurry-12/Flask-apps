from flask import Blueprint, redirect, render_template, abort, url_for
from flask_login import login_required, current_user
from ...models import Alert
from ...security.decorators import role_required

user_alerts_bp = Blueprint("user_alerts", __name__, url_prefix="/alerts")


@user_alerts_bp.route("/")
@role_required("user")
@login_required
def alerts():
    if current_user.role == "admin":
        return redirect(url_for("admin.admin_dashboard.index"))
    alerts = Alert.query.filter_by(user_id=current_user.id).all()
    return render_template("user/alerts.html", alerts=alerts)
