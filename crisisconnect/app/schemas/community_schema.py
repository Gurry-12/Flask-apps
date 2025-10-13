from marshmallow import Schema, fields
from ..models import Community


class CommunitySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(allow_none=True)
    created_at = fields.DateTime(dump_only=True)

    class Meta:
        model = Community
        fields = ("id", "name", "description", "created_at")
