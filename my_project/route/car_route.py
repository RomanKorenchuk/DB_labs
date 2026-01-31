from flask import Blueprint, jsonify, request
from my_project.controller.car_controller import CarController

car_bp = Blueprint('cars', __name__)
controller = CarController()

@car_bp.route('/cars', methods=['GET'])
def get_all_cars():
    return jsonify(controller.get_all())

@car_bp.route('/cars/<int:car_id>', methods=['GET'])
def get_car_by_id(car_id):
    car = controller.get_by_id(car_id)
    if car:
        return jsonify(car), 200
    return jsonify({"error": "Brand not found"}), 404

@car_bp.route('/cars', methods=['POST'])
def create_car():
    data = request.json
    required = ['plate_number', 'model_id', 'driver_id']
    if not data or not all(k in data for k in required):
        return jsonify({"error": f"Missing fields: {required}"}), 400
    
    try:
        return jsonify(controller.create(data)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@car_bp.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.json
    updated = controller.update(car_id, data)
    if updated:
        return jsonify(updated), 200
    return jsonify({"error": "Car not found"}), 404

@car_bp.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    deleted_obj, error = controller.delete(car_id)
    if error:
        status = 409 if "linked" in error else 404
        return jsonify({"error": error}), status
    return jsonify(deleted_obj), 200