from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from ...security.decorators import role_required

admin_reports_bp = Blueprint("admin_reports", __name__, url_prefix="/reports")


@admin_reports_bp.route("/")
@role_required("admin")
@login_required
def reports():
    if current_user.role != "admin":
        abort(403)
    return render_template("admin/reports.html")
