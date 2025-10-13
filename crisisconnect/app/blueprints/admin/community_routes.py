from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user

from ...security.decorators import role_required
from ...extensions import db
from ...models import Community
from .forms import CommunityForm

admin_community_bp = Blueprint("admin_community", __name__, url_prefix="/communities")


@admin_community_bp.route("/new", methods=["GET", "POST"])
@role_required("admin")
@login_required
def create_community():
    if current_user.role != "admin":
        abort(403)
    form = CommunityForm()
    if form.validate_on_submit():
        community = Community(name=form.name.data, description=form.description.data)
        db.session.add(community)
        db.session.commit()
        flash("Community created successfully!", "success")
        return redirect(url_for("admin.admin_dashboard.index"))
    return render_template("admin/community_form.html", form=form)


@admin_community_bp.route("/<int:community_id>/delete", methods=["POST"])
@role_required("admin")
@login_required
def delete_community(community_id):
    if current_user.role != "admin":
        abort(403)
    community = Community.query.get_or_404(community_id)
    db.session.delete(community)
    db.session.commit()
    flash("Community deleted successfully!", "success")
    return redirect(url_for("admin.admin_dashboard.index"))
