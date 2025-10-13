from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user


def role_required(*roles):
    """
    Restrict access to specific roles.
    Usage:
        @role_required("admin")
        @role_required("user", "manager")
    """

    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            # Not logged in → send to landing
            if not current_user.is_authenticated:
                flash("Please log in to access this page.", "warning")
                return redirect(url_for("main.index"))

            # Wrong role → redirect back to their dashboard
            if current_user.role not in roles:
                flash("You do not have permission to access this page.", "danger")

                if current_user.role == "user":
                    return redirect(url_for("user.user_dashboard.index"))
                elif current_user.role == "admin":
                    return redirect(url_for("admin.admin_dashboard.index"))
                else:
                    # fallback if role is something else
                    return redirect(url_for("main.index"))

            return f(*args, **kwargs)

        return wrapped

    return decorator
