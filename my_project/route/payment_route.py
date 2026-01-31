from flask import Blueprint, jsonify, request
from my_project.controller.payment_controller import PaymentController

payment_bp = Blueprint('payments', __name__)
controller = PaymentController()

@payment_bp.route('/payments', methods=['GET'])
def get_all_payments():
    return jsonify(controller.get_all())

@payment_bp.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment_by_id(payment_id):
    payment = controller.get_by_id(payment_id)
    if payment:
        return jsonify(payment), 200
    return jsonify({"error": "Brand not found"}), 404

@payment_bp.route('/payments', methods=['POST'])
def create_payment():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Field 'name' is required"}), 400
    return jsonify(controller.create(data)), 201

@payment_bp.route('/payments/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    data = request.json
    res = controller.update(payment_id, data)
    if res: return jsonify(res), 200
    return jsonify({"error": "Payment type not found"}), 404

@payment_bp.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    deleted, error = controller.delete(payment_id)
    if error:
        return jsonify({"error": error}), 409
    return jsonify(deleted), 200