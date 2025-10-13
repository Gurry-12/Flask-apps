from models import DrillLog
from app import db
from datetime import datetime

def schedule_drill(user, drill_name, date):
    drill = DrillLog(
        drill_name=drill_name,
        date=date,
        status='pending',
        user_id=user.id
    )
    db.session.add(drill)
    db.session.commit()
    return drill

def complete_drill(drill_id, user):
    drill = DrillLog.query.get(drill_id)
    if drill and drill.user_id == user.id:
        drill.status = 'completed'
        db.session.commit()
        return drill
    return None
