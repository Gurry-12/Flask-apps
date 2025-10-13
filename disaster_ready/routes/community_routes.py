from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from services.community_service import post_tip, get_all_tips

community_bp = Blueprint('community', __name__, url_prefix='/community')

@community_bp.route('/')
@login_required
def community():
    tips = get_all_tips()
    return render_template('community.html', tips=tips)

@community_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_tip():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_tip(current_user, title, content)
        flash('Tip added successfully!', 'success')
        return redirect(url_for('community.community'))
    return render_template('add_tip.html')
