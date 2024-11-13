from flask import Blueprint
from controllers.RoomController import get_rooms, get_room, add_room, update_room, delete_room

room_bp = Blueprint('room_bp', __name__)

room_bp.route('/api/rooms', methods=['GET'])(get_rooms)
room_bp.route('/api/rooms/<int:room_id>', methods=['GET'])(get_room)
room_bp.route('/api/rooms', methods=['POST'])(add_room)
room_bp.route('/api/rooms/<int:room_id>', methods=['PUT'])(update_room)
room_bp.route('/api/rooms/<int:room_id>', methods=['DELETE'])(delete_room)