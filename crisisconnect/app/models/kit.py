from ..extensions import db

class Kit(db.Model):
    __tablename__ = 'kits'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    household_id = db.Column(db.Integer, db.ForeignKey('households.id'), nullable=False)
    household = db.relationship('Household', backref=db.backref('kits', lazy=True))

    def __repr__(self):
        return f'<Kit {self.name}>'