from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ...extensions import db
from .forms import ProfileForm
from ...security.decorators import role_required

user_profile_bp = Blueprint("user_profile", __name__, url_prefix="/profile")


@user_profile_bp.route("/", methods=["GET", "POST"])
@role_required("user")
@login_required
def profile():
    if current_user.role == "admin":
        return redirect(url_for("admin.admin_dashboard.index"))
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.email = form.email.data
        if form.password.data:
            current_user.set_password(form.password.data)
        db.session.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for("user_profile.profile"))
    return render_template("user/profile.html", form=form)
