
from flask import Blueprint, jsonify, request
from my_project.controller.order_controller import OrderController

order_bp = Blueprint('orders', __name__)
controller = OrderController()

@order_bp.route('/orders', methods=['GET'])
def get_all_orders():
    return jsonify(controller.get_all())

@order_bp.route('/orders/history', methods=['GET'])
def get_orders_history():
    return jsonify(controller.get_history())

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    order = controller.get_by_id(order_id)
    if order:
        return jsonify(order), 200
    return jsonify({"error": "Brand not found"}), 404

@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    required = ['client_id', 'pickup_address', 'destination_address', 'total_price']
    if not all(k in data for k in required):
        return jsonify({"error": f"Missing fields. Required: {required}"}), 400
    
    try:
        return jsonify(controller.create(data)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@order_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    deleted_obj, error = controller.delete(order_id)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(deleted_obj), 200