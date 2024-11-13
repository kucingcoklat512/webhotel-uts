from flask import jsonify, request
from models.RoomModel import Room
from config import db

def get_rooms():
    rooms = Room.query.all()
    return jsonify([room.to_dict() for room in rooms])

def get_room(room_id):
    room = Room.query.get(room_id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    return jsonify(room.to_dict())

def add_room():
    data = request.get_json()
    new_room = Room(**data)
    db.session.add(new_room)
    db.session.commit()
    return jsonify(new_room.to_dict()), 201

def update_room(room_id):
    room = Room.query.get(room_id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(room, key, value)
    db.session.commit()
    return jsonify(room.to_dict())

def delete_room(room_id):
    room = Room.query.get(room_id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    db.session.delete(room)
    db.session.commit()
    return jsonify({'message': 'Room deleted successfully'})