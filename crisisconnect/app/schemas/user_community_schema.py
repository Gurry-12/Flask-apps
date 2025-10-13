from marshmallow import Schema, fields
from ..models import UserCommunity


class UserCommunitySchema(Schema):
    user_id = fields.Int(required=True)
    community_id = fields.Int(required=True)
    joined_at = fields.DateTime(dump_only=True)

    class Meta:
        model = UserCommunity
        fields = ("user_id", "community_id", "joined_at")
