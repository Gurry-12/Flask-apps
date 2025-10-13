from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from decorators import role_required
from app import db
from models import User, DisasterKit, Household, AlertLog, DrillLog, CommunityTip

api_bp = Blueprint('api', __name__, url_prefix='/api')

# --------------------
# USER INFO
# --------------------
@api_bp.route('/user', methods=['GET'])
@login_required
def get_user():
    return jsonify({
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role
    })


# --------------------
# HOUSEHOLDS
# --------------------
@api_bp.route('/households', methods=['GET'])
@login_required
def get_households():
    households = Household.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        "id": h.id,
        "name": h.name,
        "members": h.members,
        "pets": h.pets,
        "medical_info": h.medical_info
    } for h in households])

@api_bp.route('/households', methods=['POST'])
@login_required
def add_household():
    data = request.json
    new_h = Household(
        name=data.get('name'),
        members=data.get('members', 1),
        pets=data.get('pets', 0),
        medical_info=data.get('medical_info'),
        user_id=current_user.id
    )
    db.session.add(new_h)
    db.session.commit()
    return jsonify({"message": "Household added", "id": new_h.id})


# --------------------
# DISASTER KITS
# --------------------
@api_bp.route('/kits', methods=['GET'])
@login_required
def get_kits():
    kits = DisasterKit.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        "id": k.id,
        "kit_name": k.kit_name,
        "disaster_type": k.disaster_type,
        "items": k.items,
        "last_updated": k.last_updated
    } for k in kits])

@api_bp.route('/kits', methods=['POST'])
@login_required
def add_kit():
    data = request.json
    kit = DisasterKit(
        kit_name=data.get('kit_name'),
        disaster_type=data.get('disaster_type'),
        items=data.get('items'),
        user_id=current_user.id
    )
    db.session.add(kit)
    db.session.commit()
    return jsonify({"message": "Kit added", "id": kit.id})


# --------------------
# ALERTS
# --------------------
@api_bp.route('/alerts', methods=['GET'])
@login_required
def get_alerts():
    alerts = AlertLog.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        "id": a.id,
        "title": a.title,
        "description": a.description,
        "severity": a.severity,
        "date": a.date,
        "read": a.read
    } for a in alerts])


# --------------------
# DRILLS
# --------------------
@api_bp.route('/drills', methods=['GET'])
@login_required
def get_drills():
    drills = DrillLog.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        "id": d.id,
        "drill_name": d.drill_name,
        "date": d.date,
        "status": d.status
    } for d in drills])

@api_bp.route('/drills', methods=['POST'])
@login_required
def add_drill():
    data = request.json
    drill = DrillLog(
        drill_name=data.get('drill_name'),
        date=data.get('date'),
        status=data.get('status', 'pending'),
        user_id=current_user.id
    )
    db.session.add(drill)
    db.session.commit()
    return jsonify({"message": "Drill added", "id": drill.id})


# --------------------
# COMMUNITY TIPS
# --------------------
@api_bp.route('/tips', methods=['GET'])
@login_required
def get_tips():
    tips = CommunityTip.query.order_by(CommunityTip.date_posted.desc()).all()
    return jsonify([{
        "id": t.id,
        "title": t.title,
        "content": t.content,
        "user": t.user.name,
        "date_posted": t.date_posted
    } for t in tips])

@api_bp.route('/tips', methods=['POST'])
@login_required
def add_tip():
    data = request.json
    tip = CommunityTip(
        title=data.get('title'),
        content=data.get('content'),
        user_id=current_user.id
    )
    db.session.add(tip)
    db.session.commit()
    return jsonify({"message": "Tip added", "id": tip.id})
