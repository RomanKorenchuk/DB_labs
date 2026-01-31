from flask import Blueprint, jsonify, request
from my_project.controller.client_controller import ClientController

client_bp = Blueprint('clients', __name__)
controller = ClientController()

@client_bp.route('/clients', methods=['GET'])
def get_all_clients():
    return jsonify(controller.get_all())

@client_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client_by_id(client_id):
    client = controller.get_by_id(client_id)
    if client:
        return jsonify(client), 200
    return jsonify({"error": "Brand not found"}), 404

@client_bp.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    if not data or 'first_name' not in data or 'phone' not in data:
        return jsonify({"error": "Fields 'first_name' and 'phone' are required"}), 400
    return jsonify(controller.create(data)), 201

@client_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.json
    result = controller.update(client_id, data)
    if result:
        return jsonify(result), 200
    return jsonify({"error": "Client not found"}), 404

@client_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    deleted_obj, error = controller.delete(client_id)
    if error:
        status = 409 if "active orders" in error else 404
        return jsonify({"error": error}), status
    return jsonify(deleted_obj), 200

@client_bp.route('/clients/<int:client_id>/stats', methods=['GET'])
def get_client_stats(client_id):
    stats = controller.get_stats(client_id)
    if stats:
        return jsonify(stats), 200
    return jsonify({"error": "Client not found"}), 404