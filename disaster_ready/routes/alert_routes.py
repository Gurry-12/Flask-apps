from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from services.alert_service import create_alert, get_unread_alerts, mark_alert_read, get_all_alerts
from services.notification_service import send_alert_notification
from decorators import role_required

alert_bp = Blueprint('alert', __name__, url_prefix='/alerts')

# --------------------------
# USER ALERTS
# --------------------------
@alert_bp.route('/')
@login_required
def alerts():
    alerts = get_unread_alerts(current_user)
    return render_template('alerts.html', alerts=alerts)


@alert_bp.route('/mark_read/<int:alert_id>')
@login_required
def mark_read(alert_id):
    if mark_alert_read(alert_id, current_user):
        flash('Alert marked as read.', 'success')
    else:
        flash('Permission denied!', 'danger')
    return redirect(url_for('alert.alerts'))


@alert_bp.route('/fetch_external')
@login_required
def fetch_external_alert():
    # Example API fetch placeholder
    title = "Severe Flood Warning"
    description = "Flood expected in your area in next 24 hours."
    alert = create_alert(current_user, title, description, severity='high')
    send_alert_notification(current_user, alert)
    flash('External alert fetched and notification sent!', 'info')
    return redirect(url_for('alert.alerts'))


# --------------------------
# ADMIN ALERTS
# --------------------------
@alert_bp.route('/admin')
@login_required
@role_required('admin')
def admin_alerts():
    alerts = get_all_alerts()  # all system alerts
    return render_template('admin/admin_alerts.html', alerts=alerts)


@alert_bp.route('/admin/create')
@login_required
@role_required('admin')
def create_system_alert():
    # Example: hardcoded for now
    alert = create_alert(
        current_user,
        "System Test Alert",
        "This is a test broadcast to all users.",
        severity="medium"
    )
    send_alert_notification(current_user, alert)
    flash('System-wide alert created & broadcasted!', 'success')
    return redirect(url_for('alert.admin_alerts'))
