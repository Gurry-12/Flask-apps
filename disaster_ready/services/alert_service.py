from models import AlertLog
from app import db
from datetime import datetime

def create_alert(user, title, description, severity='medium'):
    """
    Create a new alert for a user.
    """
    alert = AlertLog(
        title=title,
        description=description,
        severity=severity,
        date=datetime.now(),
        user_id=user.id
    )
    db.session.add(alert)
    db.session.commit()
    return alert

def get_unread_alerts(user):
    """
    Retrieve unread alerts for a user.
    """
    return AlertLog.query.filter_by(user_id=user.id, read=False).order_by(AlertLog.date.desc()).all()

def mark_alert_read(alert_id, user):
    alert = AlertLog.query.get(alert_id)
    if alert and alert.user_id == user.id:
        alert.read = True
        db.session.commit()
        return True
    return False

def get_all_alerts():
    """
    Admin: Retrieve all alerts in the system.
    """
    return AlertLog.query.order_by(AlertLog.date.desc()).all()

