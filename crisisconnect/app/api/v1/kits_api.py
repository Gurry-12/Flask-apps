from flask_restx import Namespace, Resource, fields
from flask_login import login_required, current_user
from ...extensions import db
from ...models import Kit, Household
from ...schemas.kit_schema import KitSchema

api = Namespace("kits", description="Operations related to emergency kits")
kit_schema = KitSchema()
kits_schema = KitSchema(many=True)
kit_model = api.model(
    "Kit",
    {
        "id": fields.Integer(readonly=True, description="Unique kit ID"),
        "name": fields.String(required=True, description="Kit name"),
        "description": fields.String(description="Kit description"),
        "user_id": fields.Integer(
            required=True, description="ID of the user who created the kit"
        ),
        "household_id": fields.Integer(
            required=True, description="ID of the associated household"
        ),
        "created_at": fields.DateTime(
            readonly=True, description="Kit creation timestamp"
        ),
    },
)


@api.route("")
class KitList(Resource):
    @login_required
    @api.doc(
        description="Retrieve kits created by the authenticated user.",
        responses={200: "Success", 401: "Unauthorized: Must be logged in"},
        security="session",
    )
    @api.marshal_with(kit_model, envelope="data")
    def get(self):
        kits = Kit.query.filter_by(user_id=current_user.id).all()
        return kits_schema.dump(kits)

    @login_required
    @api.doc(
        description="Create a new kit associated with a household. Requires authentication.",
        responses={
            201: "Created",
            400: "Bad Request: Invalid input",
            401: "Unauthorized: Must be logged in",
            404: "Not Found: Household does not exist",
        },
        security="session",
    )
    @api.expect(kit_model)
    @api.marshal_with(kit_model, code=201)
    def post(self):
        data = api.payload
        household = Household.query.filter_by(
            id=data["household_id"], user_id=current_user.id
        ).first_or_404()
        kit = Kit(
            name=data["name"],
            description=data.get("description"),
            user_id=current_user.id,
            household_id=household.id,
        )
        db.session.add(kit)
        db.session.commit()
        return kit_schema.dump(kit), 201


@api.route("/<int:id>")
class KitResource(Resource):
    @login_required
    @api.doc(
        description="Retrieve a specific kit by ID for the authenticated user.",
        responses={
            200: "Success",
            401: "Unauthorized: Must be logged in",
            404: "Not Found: Kit does not exist or user lacks access",
        },
        security="session",
    )
    @api.marshal_with(kit_model)
    def get(self, id):
        kit = Kit.query.filter_by(id=id, user_id=current_user.id).first_or_404()
        return kit_schema.dump(kit)
