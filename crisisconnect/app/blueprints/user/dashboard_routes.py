from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from ...models import Alert, Household, Kit, Community, UserCommunity
from ...security.decorators import role_required

user_dashboard_bp = Blueprint("user_dashboard", __name__, url_prefix="/dashboard")


@user_dashboard_bp.route("/")
@role_required("user")
@login_required
def index():
    if current_user.role != "user":
        return redirect(url_for("admin.admin_dashboard.index"))
    alerts = Alert.query.filter_by(user_id=current_user.id).all()
    households = Household.query.filter_by(user_id=current_user.id).all()
    kits = Kit.query.join(Household).filter(Household.user_id == current_user.id).all()
    communities = (
        Community.query.join(UserCommunity)
        .filter(UserCommunity.user_id == current_user.id)
        .all()
    )
    return render_template(
        "user/dashboard.html",
        alerts=alerts,
        households=households,
        kits=kits,
        communities=communities,
    )
