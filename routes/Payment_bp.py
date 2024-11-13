from flask import Blueprint
from controllers.PaymentController import get_payments, get_payment, add_payment, update_payment, delete_payment

payment_bp = Blueprint('payment_bp', __name__)

payment_bp.route('/api/payments', methods=['GET'])(get_payments)
payment_bp.route('/api/payments/<int:payment_id>', methods=['GET'])(get_payment)
payment_bp.route('/api/payments', methods=['POST'])(add_payment)
payment_bp.route('/api/payments/<int:payment_id>', methods=['PUT'])(update_payment)
payment_bp.route('/api/payments/<int:payment_id>', methods=['DELETE'])(delete_payment)