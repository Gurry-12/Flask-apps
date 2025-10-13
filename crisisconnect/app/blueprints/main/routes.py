# app/blueprints/main/routes.py
from flask import Blueprint, redirect, url_for, render_template
from flask_login import current_user

from . import main_bp


@main_bp.route("/")
def index():
    # If not logged in → show landing page
    if not current_user.is_authenticated:
        return render_template("landing.html")

    # If logged in → redirect based on role
    if current_user.role == "admin":
        return redirect(url_for("admin.admin_dashboard.index"))
    elif current_user.role == "user":
        return redirect(url_for("user.user_dashboard.index"))

    # fallback
    return redirect(url_for("auth.login"))
