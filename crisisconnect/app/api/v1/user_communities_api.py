from flask_restx import Namespace, Resource, fields
from flask_login import login_required, current_user
from ...extensions import db
from ...models import UserCommunity, Community
from ...schemas.user_community_schema import UserCommunitySchema

api = Namespace(
    "user-communities", description="Operations related to user-community memberships"
)
user_community_schema = UserCommunitySchema()
user_communities_schema = UserCommunitySchema(many=True)
user_community_model = api.model(
    "UserCommunity",
    {
        "user_id": fields.Integer(required=True, description="ID of the user"),
        "community_id": fields.Integer(
            required=True, description="ID of the community"
        ),
        "joined_at": fields.DateTime(
            readonly=True, description="Timestamp when the user joined the community"
        ),
    },
)


@api.route("")
class UserCommunityList(Resource):
    @login_required
    @api.doc(
        description="Retrieve all community memberships for the authenticated user.",
        responses={200: "Success", 401: "Unauthorized: Must be logged in"},
        security="session",
    )
    @api.marshal_with(user_community_model, envelope="data")
    def get(self):
        user_communities = UserCommunity.query.filter_by(user_id=current_user.id).all()
        return user_communities_schema.dump(user_communities)

    @login_required
    @api.doc(
        description="Join a community by creating a new membership. Requires authentication.",
        responses={
            201: "Created",
            400: "Bad Request: Invalid input or user already a member",
            401: "Unauthorized: Must be logged in",
            404: "Not Found: Community does not exist",
        },
        security="session",
    )
    @api.expect(user_community_model)
    @api.marshal_with(user_community_model, code=201)
    def post(self):
        data = api.payload
        Community.query.get_or_404(data["community_id"])
        if UserCommunity.query.filter_by(
            user_id=current_user.id, community_id=data["community_id"]
        ).first():
            api.abort(400, "User is already a member of this community")
        user_community = UserCommunity(
            user_id=current_user.id, community_id=data["community_id"]
        )
        db.session.add(user_community)
        db.session.commit()
        return user_community_schema.dump(user_community), 201


@api.route("/<int:user_id>/<int:community_id>")
class UserCommunityResource(Resource):
    @login_required
    @api.doc(
        description="Retrieve a specific user-community membership. Only the authenticated user can access their own memberships.",
        responses={
            200: "Success",
            401: "Unauthorized: Must be logged in",
            403: "Forbidden: Cannot access other users' memberships",
            404: "Not Found: Membership does not exist",
        },
        security="session",
    )
    @api.marshal_with(user_community_model)
    def get(self, user_id, community_id):
        if user_id != current_user.id:
            api.abort(403, "Access forbidden")
        user_community = UserCommunity.query.filter_by(
            user_id=user_id, community_id=community_id
        ).first_or_404()
        return user_community_schema.dump(user_community)
