from flask import Blueprint
from controllers.ReservationController import get_reservations, get_reservation, add_reservation, update_reservation, delete_reservation

reservation_bp = Blueprint('reservation_bp', __name__)

reservation_bp.route('/api/reservations', methods=['GET'])(get_reservations)
reservation_bp.route('/api/reservations/<int:reservation_id>', methods=['GET'])(get_reservation)
reservation_bp.route('/api/reservations', methods=['POST'])(add_reservation)
reservation_bp.route('/api/reservations/<int:reservation_id>', methods=['PUT'])(update_reservation)
reservation_bp.route('/api/reservations/<int:reservation_id>', methods=['DELETE'])(delete_reservation)
