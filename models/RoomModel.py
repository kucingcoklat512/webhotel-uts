from config import db

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(10), nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'room_number': self.room_number,
            'room_type': self.room_type,
            'price_per_night': self.price_per_night,
            'availability': self.availability
        }