from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from ...extensions import db
from ...models import Kit, Household
from .forms import KitForm
from ...security.decorators import role_required

admin_kits_bp = Blueprint("admin_kits", __name__, url_prefix="/kits")


@admin_kits_bp.route("/new", methods=["GET", "POST"])
@role_required("admin")
@login_required
def create_kit():
    if current_user.role != "admin":
        abort(403)
    form = KitForm()
    form.household_id.choices = [(h.id, h.name) for h in Household.query.all()]
    if form.validate_on_submit():
        kit = Kit(
            name=form.name.data,
            description=form.description.data,
            household_id=form.household_id.data,
        )
        db.session.add(kit)
        db.session.commit()
        flash("Kit created successfully!", "success")
        return redirect(url_for("admin.admin_dashboard.index"))
    return render_template("admin/kit_form.html", form=form)


@admin_kits_bp.route("/<int:kit_id>/delete", methods=["POST"])
@role_required("admin")
@login_required
def delete_kit(kit_id):
    if current_user.role != "admin":
        abort(403)
    kit = Kit.query.get_or_404(kit_id)
    db.session.delete(kit)
    db.session.commit()
    flash("Kit deleted successfully!", "success")
    return redirect(url_for("admin.admin_dashboard.index"))
