from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='user')  # 'user', 'admin'

    households = db.relationship('Household', backref='owner', lazy=True)
    kits = db.relationship('DisasterKit', backref='owner', lazy=True)
    drills = db.relationship('DrillLog', backref='user', lazy=True)
    alerts = db.relationship('AlertLog', backref='user', lazy=True)
    tips = db.relationship('CommunityTip', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Household(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    members = db.Column(db.Integer, default=1)
    pets = db.Column(db.Integer, default=0)
    medical_info = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class DisasterKit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kit_name = db.Column(db.String(100))
    disaster_type = db.Column(db.String(50))
    items = db.Column(db.Text)  # JSON string of items & quantities
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class DrillLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drill_name = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50))  # completed, pending
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class AlertLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    severity = db.Column(db.String(50))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    read = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

class CommunityTip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
