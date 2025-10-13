from marshmallow import Schema, fields
from ..models import Kit


class KitSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(allow_none=True)
    household_id = fields.Int(required=True)

    class Meta:
        model = Kit
        fields = ("id", "name", "description", "household_id")
