from ..extensions import db
from ..models import Kit, Household


class KitService:
    def create_kit(self, name, description, user_id, household_id):
        Household.query.get_or_404(household_id)
        kit = Kit(
            name=name,
            description=description,
            household_id=household_id,
        )
        db.session.add(kit)
        db.session.commit()
        return kit
