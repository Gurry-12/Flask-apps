from marshmallow import Schema, fields
from ..models import Alert


class AlertSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(allow_none=True)
    severity = fields.Str(
        required=True, validate=lambda x: x in ["Low", "Medium", "High"]
    )
    created_at = fields.DateTime(dump_only=True)
    user_id = fields.Int(required=True)

    class Meta:
        model = Alert
        fields = ("id", "title", "description", "severity", "created_at", "user_id")
