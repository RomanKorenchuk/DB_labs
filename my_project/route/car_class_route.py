from flask import Blueprint, jsonify, request
from my_project.controller.car_class_controller import CarClassController

class_bp = Blueprint('classes', __name__)
controller = CarClassController()

@class_bp.route('/classes', methods=['GET'])
def get_all_classes():
    return jsonify(controller.get_all())

@class_bp.route('/classes/<int:class_id>/cars', methods=['GET'])
def get_cars_by_class(class_id):
    data = controller.get_cars(class_id)
    if data:
        return jsonify(data), 200
    return jsonify({"error": "Class not found"}), 404

@class_bp.route('/classes/<int:class_id>', methods=['GET'])
def get_class_by_id(class_id):
    data = controller.get_by_id(class_id)
    if data:
        return jsonify(data), 200
    return jsonify({"error": "Brand not found"}), 404

@class_bp.route('/classes', methods=['POST'])
def create_class():
    data = request.json
    if not data or 'name' not in data or 'base_rate' not in data:
        return jsonify({"error": "Fields 'name' and 'base_rate' are required"}), 400
    return jsonify(controller.create(data)), 201

@class_bp.route('/classes/<int:class_id>', methods=['PUT'])
def update_class(class_id):
    data = request.json
    res = controller.update(class_id, data)
    if res: return jsonify(res), 200
    return jsonify({"error": "Class not found"}), 404

@class_bp.route('/classes/<int:class_id>', methods=['DELETE'])
def delete_class(class_id):
    deleted, error = controller.delete(class_id)
    if error:
        status = 409 if "linked" in error else 404
        return jsonify({"error": error}), status
    return jsonify(deleted), 200