from config import app, db
from routes.Guest_bp import guest_bp
from routes.Room_bp import room_bp
from routes.Reservation_bp import reservation_bp
from routes.Payment_bp import payment_bp

app.register_blueprint(guest_bp)
app.register_blueprint(room_bp)
app.register_blueprint(reservation_bp)
app.register_blueprint(payment_bp)

db.create_all()

#if __name__ == '__main__':
#    app.run(debug=True)
