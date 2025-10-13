from flask_restx import Namespace, Resource, fields
from flask_login import login_required
from ...extensions import db
from ...models import User
from ...schemas.user_schema import UserSchema

api = Namespace("users", description="Operations related to users")
user_schema = UserSchema()
users_schema = UserSchema(many=True)
user_model = api.model(
    "User",
    {
        "id": fields.Integer(readonly=True, description="Unique user ID"),
        "username": fields.String(required=True, description="Unique username"),
        "email": fields.String(required=True, description="User email address"),
        "created_at": fields.DateTime(
            readonly=True, description="Account creation timestamp"
        ),
    },
)


@api.route("")
class UserList(Resource):
    @login_required
    @api.doc(
        description="Retrieve a list of all users. Requires authentication.",
        responses={
            200: "Success",
            401: "Unauthorized: Must be logged in",
            403: "Forbidden: Insufficient permissions",
        },
        security="session",
    )
    @api.marshal_with(user_model, envelope="data")
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)


@api.route("/<int:id>")
class UserResource(Resource):
    @login_required
    @api.doc(
        description="Retrieve a specific user by ID. Requires authentication.",
        responses={
            200: "Success",
            401: "Unauthorized: Must be logged in",
            404: "Not Found: User does not exist",
        },
        security="session",
    )
    @api.marshal_with(user_model)
    def get(self, id):
        user = User.query.get_or_404(id)
        return user_schema.dump(user)
