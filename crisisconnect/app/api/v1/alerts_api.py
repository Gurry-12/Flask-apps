from flask_restx import Namespace, Resource, fields
from flask_login import login_required, current_user
from ...extensions import db
from ...models import Alert
from ...schemas.alert_schema import AlertSchema

api = Namespace("alerts", description="Operations related to alerts")
alert_schema = AlertSchema()
alerts_schema = AlertSchema(many=True)
alert_model = api.model(
    "Alert",
    {
        "id": fields.Integer(readonly=True, description="Unique alert ID"),
        "title": fields.String(required=True, description="Alert title"),
        "description": fields.String(description="Alert description"),
        "severity": fields.String(
            required=True, description="Alert severity (e.g., Low, Medium, High)"
        ),
        "created_at": fields.DateTime(
            readonly=True, description="Alert creation timestamp"
        ),
        "user_id": fields.Integer(
            required=True, description="ID of the user who created the alert"
        ),
    },
)


@api.route("")
class AlertList(Resource):
    @login_required
    @api.doc(
        description="Retrieve alerts created by the authenticated user.",
        responses={200: "Success", 401: "Unauthorized: Must be logged in"},
        security="session",
    )
    @api.marshal_with(alert_model, envelope="data")
    def get(self):
        alerts = Alert.query.filter_by(user_id=current_user.id).all()
        return alerts_schema.dump(alerts)

    @login_required
    @api.doc(
        description="Create a new alert. Requires authentication.",
        responses={
            201: "Created",
            400: "Bad Request: Invalid input",
            401: "Unauthorized: Must be logged in",
        },
        security="session",
    )
    @api.expect(alert_model)
    @api.marshal_with(alert_model, code=201)
    def post(self):
        data = api.payload
        alert = Alert(
            title=data["title"],
            description=data.get("description"),
            severity=data["severity"],
            user_id=current_user.id,
        )
        db.session.add(alert)
        db.session.commit()
        return alert_schema.dump(alert), 201


@api.route("/<int:id>")
class AlertResource(Resource):
    @login_required
    @api.doc(
        description="Retrieve a specific alert by ID for the authenticated user.",
        responses={
            200: "Success",
            401: "Unauthorized: Must be logged in",
            404: "Not Found: Alert does not exist or user lacks access",
        },
        security="session",
    )
    @api.marshal_with(alert_model)
    def get(self, id):
        alert = Alert.query.filter_by(id=id, user_id=current_user.id).first_or_404()
        return alert_schema.dump(alert)
