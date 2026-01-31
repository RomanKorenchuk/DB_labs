from flask import Blueprint, jsonify, request
from my_project.controller.car_model_controller import CarModelController

model_bp = Blueprint('models', __name__)
controller = CarModelController()

@model_bp.route('/models', methods=['GET'])
def get_all_models():
    return jsonify(controller.get_all())

@model_bp.route('/models/<int:model_id>', methods=['GET'])
def get_model_by_id(model_id):
    model = controller.get_by_id(model_id)
    if model:
        return jsonify(model), 200
    return jsonify({"error": "Brand not found"}), 404

@model_bp.route('/models', methods=['POST'])
def create_model():
    data = request.json
    if not data or 'name' not in data or 'brand_id' not in data:
        return jsonify({"error": "Fields 'name' and 'brand_id' are required"}), 400
    return jsonify(controller.create(data)), 201

@model_bp.route('/models/<int:model_id>', methods=['PUT'])
def update_model(model_id):
    data = request.json
    result = controller.update(model_id, data)
    if result:
        return jsonify(result), 200
    return jsonify({"error": "Model not found"}), 404

@model_bp.route('/models/<int:model_id>', methods=['DELETE'])
def delete_model(model_id):
    deleted_obj, error = controller.delete(model_id)
    if error:
        status = 409 if "linked" in error else 404
        return jsonify({"error": error}), status
    return jsonify(deleted_obj), 200

@model_bp.route('/models/<int:model_id>/fleet', methods=['GET'])
def get_model_fleet(model_id):
    data = controller.get_fleet(model_id)
    if data:
        return jsonify(data), 200
    return jsonify({"error": "Model not found"}), 404