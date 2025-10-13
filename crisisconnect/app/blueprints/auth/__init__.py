from flask import Blueprint

# app/blueprints/auth/__init__.py
auth_bp = Blueprint(
    "auth", __name__, template_folder="templates", static_folder="static"
)


from . import routes
