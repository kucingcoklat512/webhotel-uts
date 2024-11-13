from config import db

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'guest_id': self.guest_id,
            'room_id': self.room_id,
            'check_in_date': str(self.check_in_date),
            'check_out_date': str(self.check_out_date),
            'status': self.status
        }