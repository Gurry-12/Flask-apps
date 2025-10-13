from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from models import Household

household_bp = Blueprint('household', __name__, url_prefix='/household')

@household_bp.route('/')
@login_required
def list_households():
    households = Household.query.filter_by(user_id=current_user.id).all()
    return render_template('household.html', households=households)

@household_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_household():
    if request.method == 'POST':
        name = request.form.get('name')
        members = request.form.get('members')
        pets = request.form.get('pets')
        medical_info = request.form.get('medical_info')
        new_household = Household(name=name, members=members, pets=pets, medical_info=medical_info, user_id=current_user.id)
        db.session.add(new_household)
        db.session.commit()
        flash('Household added successfully!', 'success')
        return redirect(url_for('household.list_households'))
    return render_template('add_household.html')
