from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from ...security.decorators import role_required

admin_system_bp = Blueprint("admin_system", __name__, url_prefix="/system")


@admin_system_bp.route("/")
@role_required("admin")
@login_required
def system():
    if current_user.role != "admin":
        abort(403)
    return render_template("admin/system.html")
