from flask import Blueprint, render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from ...models import Household
from ...security.decorators import role_required

user_households_bp = Blueprint("user_households", __name__, url_prefix="/households")


@user_households_bp.route("/")
@role_required("user")
@login_required
def households():
    if current_user.role == "admin":
        return redirect(url_for("admin.admin_dashboard.index"))
    households = Household.query.filter_by(user_id=current_user.id).all()
    return render_template("user/household.html", households=households)
