from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from ...extensions import db
from ...models import Household, User
from .forms import HouseholdForm
from ...security.decorators import role_required

admin_households_bp = Blueprint("admin_households", __name__, url_prefix="/households")


@admin_households_bp.route("/new", methods=["GET", "POST"])
@role_required("admin")
@login_required
def create_household():
    if current_user.role != "admin":
        abort(403)
    form = HouseholdForm()
    form.user_id.choices = [(u.id, u.email) for u in User.query.all()]
    if form.validate_on_submit():
        household = Household(
            name=form.name.data, address=form.address.data, user_id=form.user_id.data
        )
        db.session.add(household)
        db.session.commit()
        flash("Household created successfully!", "success")
        return redirect(url_for("admin.admin_dashboard.index"))
    return render_template("admin/household_form.html", form=form)


@admin_households_bp.route("/<int:household_id>/delete", methods=["POST"])
@role_required("admin")
@login_required
def delete_household(household_id):
    if current_user.role != "admin":
        abort(403)
    household = Household.query.get_or_404(household_id)
    db.session.delete(household)
    db.session.commit()
    flash("Household deleted successfully!", "success")
    return redirect(url_for("admin.admin_dashboard.index"))
