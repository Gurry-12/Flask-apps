from flask_restx import Namespace, Resource, fields
from flask_login import login_required, current_user
from ...extensions import db
from ...models import Community, UserCommunity
from ...schemas.community_schema import CommunitySchema

api = Namespace("communities", description="Operations related to communities")
community_schema = CommunitySchema()
communities_schema = CommunitySchema(many=True)
community_model = api.model(
    "Community",
    {
        "id": fields.Integer(readonly=True, description="Unique community ID"),
        "name": fields.String(required=True, description="Community name"),
        "description": fields.String(description="Community description"),
        "created_at": fields.DateTime(
            readonly=True, description="Community creation timestamp"
        ),
    },
)


@api.route("")
class CommunityList(Resource):
    @login_required
    @api.doc(
        description="Retrieve communities the authenticated user is part of.",
        responses={200: "Success", 401: "Unauthorized: Must be logged in"},
        security="session",
    )
    @api.marshal_with(community_model, envelope="data")
    def get(self):
        communities = (
            Community.query.join(UserCommunity)
            .filter(UserCommunity.user_id == current_user.id)
            .all()
        )
        return communities_schema.dump(communities)

    @login_required
    @api.doc(
        description="Create a new community. The creator is automatically added as a member. Requires authentication.",
        responses={
            201: "Created",
            400: "Bad Request: Invalid input",
            401: "Unauthorized: Must be logged in",
        },
        security="session",
    )
    @api.expect(community_model)
    @api.marshal_with(community_model, code=201)
    def post(self):
        data = api.payload
        community = Community(name=data["name"], description=data.get("description"))
        db.session.add(community)
        db.session.commit()
        user_community = UserCommunity(
            user_id=current_user.id, community_id=community.id
        )
        db.session.add(user_community)
        db.session.commit()
        return community_schema.dump(community), 201


@api.route("/<int:id>")
class CommunityResource(Resource):
    @login_required
    @api.doc(
        description="Retrieve a specific community by ID for the authenticated user.",
        responses={
            200: "Success",
            401: "Unauthorized: Must be logged in",
            404: "Not Found: Community does not exist or user is not a member",
        },
        security="session",
    )
    @api.marshal_with(community_model)
    def get(self, id):
        community = (
            Community.query.join(UserCommunity)
            .filter(Community.id == id, UserCommunity.user_id == current_user.id)
            .first_or_404()
        )
        return community_schema.dump(community)
