from models import CommunityTip
from app import db
from datetime import datetime

def post_tip(user, title, content):
    tip = CommunityTip(
        title=title,
        content=content,
        user_id=user.id,
        date_posted=datetime.utcnow()
    )
    db.session.add(tip)
    db.session.commit()
    return tip

def get_all_tips():
    return CommunityTip.query.order_by(CommunityTip.date_posted.desc()).all()

