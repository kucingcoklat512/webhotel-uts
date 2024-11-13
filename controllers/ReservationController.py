from flask import jsonify, request
from models.ReservationModel import Reservation
from config import db

def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([reservation.to_dict() for reservation in reservations])

def get_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    if not reservation:
        return jsonify({'error': 'Reservation not found'}), 404
    return jsonify(reservation.to_dict())

def add_reservation():
    data = request.get_json()
    new_reservation = Reservation(**data)
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify(new_reservation.to_dict()), 201

def update_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    if not reservation:
        return jsonify({'error': 'Reservation not found'}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(reservation, key, value)
    db.session.commit()
    return jsonify(reservation.to_dict())

def delete_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    if not reservation:
        return jsonify({'error': 'Reservation not found'}), 404
    db.session.delete(reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation deleted successfully'})