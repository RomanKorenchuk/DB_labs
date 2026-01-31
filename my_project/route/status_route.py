from flask import Blueprint, jsonify, request
from my_project.controller.status_controller import StatusController

status_bp = Blueprint('statuses', __name__)
controller = StatusController()

@status_bp.route('/statuses', methods=['GET'])
def get_all_statuses():
    return jsonify(controller.get_all())

@status_bp.route('/statuses/<int:status_id>', methods=['GET'])
def get_brand_by_id(status_id):
    status = controller.get_by_id(status_id)
    if status:
        return jsonify(status), 200
    return jsonify({"error": "Brand not found"}), 404

@status_bp.route('/statuses', methods=['POST'])
def create_status():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Field 'name' is required"}), 400
    return jsonify(controller.create(data)), 201

@status_bp.route('/statuses/<int:status_id>', methods=['PUT'])
def update_status(status_id):
    data = request.json
    res = controller.update(status_id, data)
    if res: return jsonify(res), 200
    return jsonify({"error": "Status not found"}), 404

@status_bp.route('/statuses/<int:status_id>', methods=['DELETE'])
def delete_status(status_id):
    deleted, error = controller.delete(status_id)
    if error:
        return jsonify({"error": error}), 409
    return jsonify(deleted), 200