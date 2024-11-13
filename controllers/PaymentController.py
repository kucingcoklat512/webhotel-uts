from flask import jsonify, request
from models.PaymentModel import Payment
from config import db

def get_payments():
    payments = Payment.query.all()
    return jsonify([payment.to_dict() for payment in payments])

def get_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'error': 'Payment not found'}), 404
    return jsonify(payment.to_dict())

def add_payment():
    data = request.get_json()
    new_payment = Payment(**data)
    db.session.add(new_payment)
    db.session.commit()
    return jsonify(new_payment.to_dict()), 201

def update_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'error': 'Payment not found'}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(payment, key, value)
    db.session.commit()
    return jsonify(payment.to_dict())

def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'error': 'Payment not found'}), 404
    db.session.delete(payment)
    db.session.commit()
    return jsonify({'message': 'Payment deleted successfully'})
