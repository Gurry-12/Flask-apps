from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user

from ...security.decorators import role_required
from ...extensions import db
from ...models import Alert, User
from .forms import AlertForm

admin_alerts_bp = Blueprint("admin_alerts", __name__, url_prefix="/alerts")


@admin_alerts_bp.route("/new", methods=["GET", "POST"])
@role_required("admin")
@login_required
def create_alert():
    if current_user.role != "admin":
        abort(403)
    form = AlertForm()
    form.user_id.choices = [(u.id, u.email) for u in User.query.all()]
    if form.validate_on_submit():
        alert = Alert(
            title=form.title.data,
            description=form.description.data,
            severity=form.severity.data,
            user_id=form.user_id.data,
        )
        db.session.add(alert)
        db.session.commit()
        flash("Alert created successfully!", "success")
        return redirect(url_for("admin.admin_dashboard.index"))
    return render_template("admin/alert_form.html", form=form)


@admin_alerts_bp.route("/<int:alert_id>/delete", methods=["POST"])
@role_required("admin")
@login_required
def delete_alert(alert_id):
    if current_user.role != "admin":
        abort(403)
    alert = Alert.query.get_or_404(alert_id)
    db.session.delete(alert)
    db.session.commit()
    flash("Alert deleted successfully!", "success")
    return redirect(url_for("admin.admin_dashboard.index"))
