from ..extensions import db
from ..models import Community, UserCommunity


class CommunityService:
    def create_community(self, name, description, creator_id):
        community = Community(name=name, description=description)
        db.session.add(community)
        db.session.commit()
        user_community = UserCommunity(user_id=creator_id, community_id=community.id)
        db.session.add(user_community)
        db.session.commit()
        return community
