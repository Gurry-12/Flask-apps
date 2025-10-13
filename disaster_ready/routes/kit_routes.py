from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from services.kit_service import generate_kit
from models import DisasterKit

kit_bp = Blueprint('kit', __name__, url_prefix='/kit')

@kit_bp.route('/')
@login_required
def kit_customizer():
    # Fetch all user kits
    kits = DisasterKit.query.filter_by(user_id=current_user.id).all()
    return render_template('kit_customizer.html', kits=kits)

@kit_bp.route('/generate/<disaster_type>')
@login_required
def generate(disaster_type):
    # Use kit_service to generate kit
    kit_items = generate_kit(current_user, disaster_type)
    flash(f'{disaster_type} kit generated successfully!', 'success')
    return redirect(url_for('kit.kit_customizer'))

@kit_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_kit():
    if request.method == 'POST':
        kit_name = request.form.get('kit_name')
        disaster_type = request.form.get('disaster_type')
        items = request.form.get('items')  # JSON string
        new_kit = DisasterKit(
            kit_name=kit_name,
            disaster_type=disaster_type,
            items=items,
            user_id=current_user.id
        )
        db.session.add(new_kit)
        db.session.commit()
        flash('Kit added successfully!', 'success')
        return redirect(url_for('kit.kit_customizer'))
    return render_template('add_kit.html')
