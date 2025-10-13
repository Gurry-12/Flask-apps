from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from ...extensions import db
from ...models import Community, UserCommunity
from .forms import JoinCommunityForm
from ...security.decorators import role_required

user_community_bp = Blueprint("user_community", __name__, url_prefix="/communities")


@user_community_bp.route("/", methods=["GET", "POST"])
@role_required("user")
@login_required
def communities():
    if current_user.role == "admin":
        return redirect(url_for("admin.admin_dashboard.index"))
    join_form = JoinCommunityForm()
    join_form.community_id.choices = [(c.id, c.name) for c in Community.query.all()]
    if request.method == "POST" and join_form.validate_on_submit():
        community_id = join_form.community_id.data
        if UserCommunity.query.filter_by(
            user_id=current_user.id, community_id=community_id
        ).first():
            flash("You are already a member of this community.", "error")
        else:
            Community.query.get_or_404(community_id)
            user_community = UserCommunity(
                user_id=current_user.id, community_id=community_id
            )
            db.session.add(user_community)
            db.session.commit()
            flash("Joined community successfully!", "success")
        return redirect(url_for("user_community.communities"))
    communities = (
        Community.query.join(UserCommunity)
        .filter(UserCommunity.user_id == current_user.id)
        .all()
    )
    all_communities = Community.query.all()
    return render_template(
        "user/communities.html",
        join_form=join_form,
        communities=communities,
        all_communities=all_communities,
    )


@user_community_bp.route("/leave/<int:community_id>", methods=["POST"])
@role_required("user")
@login_required
def leave_community(community_id):
    if current_user.role == "admin":
        return redirect(url_for("admin.admin_dashboard.index"))
    user_community = UserCommunity.query.filter_by(
        user_id=current_user.id, community_id=community_id
    ).first()
    if not user_community:
        flash("You are not a member of this community.", "error")
    else:
        db.session.delete(user_community)
        db.session.commit()
        flash("Left community successfully!", "success")
    return redirect(url_for("user_community.communities"))
