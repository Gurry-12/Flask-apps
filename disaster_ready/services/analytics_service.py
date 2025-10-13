from models import DisasterKit, DrillLog, Household

def readiness_score(user):
    """
    Calculate user readiness score (0-100) based on kits, drills, and household data.
    """
    score = 0
    kits = DisasterKit.query.filter_by(user_id=user.id).all()
    drills = DrillLog.query.filter_by(user_id=user.id).all()
    households = Household.query.filter_by(user_id=user.id).all()

    if kits: score += 40
    if drills:
        completed_drills = sum(1 for d in drills if d.status.lower() == 'completed')
        score += min(completed_drills * 10, 30)
    if households: score += 30
    return min(score, 100)
