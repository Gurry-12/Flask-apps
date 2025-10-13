from models import Household, DisasterKit
from app import db
import json
from datetime import datetime

def generate_kit(user, disaster_type):
    """
    Generate a personalized disaster kit based on user's households and disaster type.
    Returns a dictionary of items.
    """
    households = Household.query.filter_by(user_id=user.id).all()
    kit_items = {}

    for household in households:
        # Base essentials
        kit_items['Water (liters)'] = household.members * 3
        kit_items['Non-perishable food (days)'] = household.members * 3
        kit_items['First aid kit'] = 1
        kit_items['Medications'] = 1 if household.medical_info else 0
        kit_items['Pet food'] = household.pets * 2

        # Disaster-specific items
        if disaster_type.lower() == 'earthquake':
            kit_items['Helmet'] = household.members
        elif disaster_type.lower() == 'flood':
            kit_items['Waterproof bags'] = 1
        elif disaster_type.lower() == 'storm':
            kit_items['Flashlight'] = household.members

    # Save or update kit
    kit = DisasterKit.query.filter_by(user_id=user.id, disaster_type=disaster_type).first()
    if kit:
        kit.items = json.dumps(kit_items)
        kit.last_updated = datetime.utcnow()
    else:
        kit = DisasterKit(
            kit_name=f"{disaster_type} Kit",
            disaster_type=disaster_type,
            items=json.dumps(kit_items),
            user_id=user.id,
            last_updated=datetime.utcnow()
        )
        db.session.add(kit)
    db.session.commit()
    return kit_items
