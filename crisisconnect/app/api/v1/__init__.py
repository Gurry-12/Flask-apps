from flask import Blueprint
from flask_restx import Api
from .users_api import api as users_api
from .alerts_api import api as alerts_api
from .households_api import api as households_api
from .kits_api import api as kits_api
from .community_api import api as communities_api
from .user_communities_api import api as user_communities_api
from ..errors import register_error_handlers

api_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")
api = Api(
    api_bp,
    title="CrisisConnect API",
    description="RESTful API for CrisisConnect, a platform for disaster preparedness and response. "
    "All endpoints require authentication via a session cookie obtained after logging in at /login. "
    "Use the Swagger UI to explore endpoints and test requests.",
    version="1.0",
)
api.add_namespace(users_api)
api.add_namespace(alerts_api)
api.add_namespace(households_api)
api.add_namespace(kits_api)
api.add_namespace(communities_api)
api.add_namespace(user_communities_api)
register_error_handlers(api)
