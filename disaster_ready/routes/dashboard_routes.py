from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import DisasterKit, DrillLog, User
from services.analytics_service import readiness_score
from decorators import role_required

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# ================================
# USER DASHBOARD
# ================================
@dashboard_bp.route('/')
@login_required
@role_required('user')
def dashboard():
    score = readiness_score(current_user)

    kits = DisasterKit.query.filter_by(user_id=current_user.id).all()
    drills = DrillLog.query.filter_by(user_id=current_user.id).all()

    dashboard_cards = [
        {"title": "Disaster Kits", "description": f"You have {len(kits)} kits"},
        {"title": "Drill Logs", "description": f"You have {len(drills)} drills logged"},
    ]

    chart_data = [score, 100 - score]

    return render_template(
        'dashboard.html',
        readiness_score=score,
        kits=kits,
        drills=drills,
        dashboard_cards=dashboard_cards,
        chart_data=chart_data
    )


# ================================
# ADMIN DASHBOARD
# ================================
@dashboard_bp.route('/admin')
@login_required
@role_required('admin')
def admin_dashboard():
    users = User.query.all()

    user_scores = [
        {
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "score": readiness_score(user)
        }
        for user in users
    ]

    avg_score = round(sum(u["score"] for u in user_scores) / len(user_scores), 2) if user_scores else 0

    roles_count = {
        "User": sum(1 for u in user_scores if u["role"] == "user"),
        "Admin": sum(1 for u in user_scores if u["role"] == "admin"),
    }

    return render_template(
        'admin_dashboard.html',
        users=user_scores,
        avg_score=avg_score,
        roles_count=roles_count
    )
