from flask import Blueprint, render_template, redirect, session, url_for, flash
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, SignupForm
from ...extensions import db
from ...models import User
from ...security.hashing import hash_password, verify_password

from . import auth_bp


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and verify_password(form.password.data, user.password_hash):
            login_user(user)
            flash("Login successful!", "success")
            if user.role == "admin":
                return redirect(url_for("admin.admin_dashboard.index"))
            return redirect(url_for("user.user_dashboard.index"))
        flash("Invalid email or password.", "error")
    return render_template("auth/login.html", form=form)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash("Email already registered.", "error")
            return render_template("auth/signup.html", form=form)
        if User.query.filter_by(username=form.username.data).first():
            flash("Username already taken.", "error")
            return render_template("auth/signup.html", form=form)
        user = User(
            username=form.username.data,
            email=form.email.data,
            role="user",  # Force user role for security
            password_hash=hash_password(form.password.data),
        )
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("auth.login"))
    return render_template("auth/signup.html", form=form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    session.clear()
    flash("Session cleared. You have been logged out.", "info")
    return redirect(url_for("main.index"))
