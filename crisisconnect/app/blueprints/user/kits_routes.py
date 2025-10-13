from flask import Blueprint, render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from ...models import Kit, Household
from ...security.decorators import role_required

user_kits_bp = Blueprint("user_kits", __name__, url_prefix="/kits")


@user_kits_bp.route("/")
@role_required("user")
@login_required
def kits():
    if current_user.role == "admin":
        return redirect(url_for("admin.admin_dashboard.index"))
    kits = Kit.query.join(Household).filter(Household.user_id == current_user.id).all()
    return render_template("user/kit.html", kits=kits)
