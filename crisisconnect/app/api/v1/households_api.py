from flask_restx import Namespace, Resource, fields
from flask_login import login_required, current_user
from ...extensions import db
from ...models import Household
from ...schemas.household_schema import HouseholdSchema

api = Namespace("households", description="Operations related to households")
household_schema = HouseholdSchema()
households_schema = HouseholdSchema(many=True)
household_model = api.model(
    "Household",
    {
        "id": fields.Integer(readonly=True, description="Unique household ID"),
        "name": fields.String(required=True, description="Household name"),
        "address": fields.String(description="Household address"),
        "user_id": fields.Integer(
            required=True, description="ID of the user who created the household"
        ),
        "created_at": fields.DateTime(
            readonly=True, description="Household creation timestamp"
        ),
    },
)


@api.route("")
class HouseholdList(Resource):
    @login_required
    @api.doc(
        description="Retrieve households created by the authenticated user.",
        responses={200: "Success", 401: "Unauthorized: Must be logged in"},
        security="session",
    )
    @api.marshal_with(household_model, envelope="data")
    def get(self):
        households = Household.query.filter_by(user_id=current_user.id).all()
        return households_schema.dump(households)

    @login_required
    @api.doc(
        description="Create a new household. Requires authentication.",
        responses={
            201: "Created",
            400: "Bad Request: Invalid input",
            401: "Unauthorized: Must be logged in",
        },
        security="session",
    )
    @api.expect(household_model)
    @api.marshal_with(household_model, code=201)
    def post(self):
        data = api.payload
        household = Household(
            name=data["name"], address=data.get("address"), user_id=current_user.id
        )
        db.session.add(household)
        db.session.commit()
        return household_schema.dump(household), 201


@api.route("/<int:id>")
class HouseholdResource(Resource):
    @login_required
    @api.doc(
        description="Retrieve a specific household by ID for the authenticated user.",
        responses={
            200: "Success",
            401: "Unauthorized: Must be logged in",
            404: "Not Found: Household does not exist or user lacks access",
        },
        security="session",
    )
    @api.marshal_with(household_model)
    def get(self, id):
        household = Household.query.filter_by(
            id=id, user_id=current_user.id
        ).first_or_404()
        return household_schema.dump(household)
