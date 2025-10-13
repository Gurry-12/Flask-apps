from flask_restx import Api
from werkzeug.exceptions import NotFound, Unauthorized


def register_error_handlers(api: Api):
    @api.errorhandler(NotFound)
    def handle_not_found(error):
        return {"message": str(error)}, 404

    @api.errorhandler(Unauthorized)
    def handle_unauthorized(error):
        return {"message": "Unauthorized access"}, 401
