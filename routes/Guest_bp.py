from flask import Blueprint
from controllers.GuestController import get_guests, get_guest, add_guest, update_guest, delete_guest

guest_bp = Blueprint('guest_bp', __name__)

guest_bp.route('/api/guests', methods=['GET'])(get_guests)
guest_bp.route('/api/guests/<int:guest_id>', methods=['GET'])(get_guest)
guest_bp.route('/api/guests', methods=['POST'])(add_guest)
guest_bp.route('/api/guests/<int:guest_id>', methods=['PUT'])(update_guest)
guest_bp.route('/api/guests/<int:guest_id>', methods=['DELETE'])(delete_guest)