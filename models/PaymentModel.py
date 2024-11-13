from config import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'reservation_id': self.reservation_id,
            'payment_date': str(self.payment_date),
            'amount': self.amount,
            'payment_method': self.payment_method
        }
