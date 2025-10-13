from marshmallow import Schema, fields
from ..models import Household


class HouseholdSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    address = fields.Str(allow_none=True)
    user_id = fields.Int(required=True)

    class Meta:
        model = Household
        fields = ("id", "name", "address", "user_id")
