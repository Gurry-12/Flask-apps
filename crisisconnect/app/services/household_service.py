from ..extensions import db
from ..models import Household


class HouseholdService:
    def create_household(self, name, address, user_id):
        household = Household(name=name, address=address, user_id=user_id)
        db.session.add(household)
        db.session.commit()
        return household
