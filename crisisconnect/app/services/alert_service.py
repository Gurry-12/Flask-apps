from ..extensions import db
from ..models import Alert


class AlertService:
    def create_alert(self, title, description, severity, user_id):
        alert = Alert(
            title=title, description=description, severity=severity, user_id=user_id
        )
        db.session.add(alert)
        db.session.commit()
        return alert
