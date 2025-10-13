from ..extensions import db


class UserCommunity(db.Model):
    __tablename__ = "user_communities"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    community_id = db.Column(
        db.Integer, db.ForeignKey("communities.id"), primary_key=True
    )
    joined_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    user = db.relationship(
        "User", backref=db.backref("community_memberships", lazy=True)
    )
    community = db.relationship("Community", backref=db.backref("members", lazy=True))

    def __repr__(self):
        return (
            f"<UserCommunity user_id={self.user_id} community_id={self.community_id}>"
        )
