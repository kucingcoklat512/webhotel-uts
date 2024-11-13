from flask import jsonify, request
from models.GuestModel import Guest
from config import db

def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

def get_guest(guest_id):
    guest = Guest.query.get(guest_id)
    if not guest:
        return jsonify({'error': 'Guest not found'}), 404
    return jsonify(guest.to_dict())

def add_guest():
    data = request.get_json()
    new_guest = Guest(**data)
    db.session.add(new_guest)
    db.session.commit()
    return jsonify(new_guest.to_dict()), 201

def update_guest(guest_id):
    guest = Guest.query.get(guest_id)
    if not guest:
        return jsonify({'error': 'Guest not found'}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(guest, key, value)
    db.session.commit()
    return jsonify(guest.to_dict())

def delete_guest(guest_id):
    guest = Guest.query.get(guest_id)
    if not guest:
        return jsonify({'error': 'Guest not found'}), 404
    db.session.delete(guest)
    db.session.commit()
    return jsonify({'message': 'Guest deleted successfully'})