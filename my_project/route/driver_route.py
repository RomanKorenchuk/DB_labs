from flask import Blueprint, jsonify, request
from my_project.controller.driver_controller import DriverController

driver_bp = Blueprint('drivers', __name__)
controller = DriverController()

@driver_bp.route('/drivers', methods=['GET'])
def get_all_drivers():
    return jsonify(controller.get_all())

@driver_bp.route('/drivers/available', methods=['GET'])
def get_available_drivers():
    return jsonify(controller.get_available())

@driver_bp.route('/drivers/<int:driver_id>', methods=['GET'])
def get_driver_by_id(driver_id):
    driver = controller.get_by_id(driver_id)
    if driver:
        return jsonify(driver), 200
    return jsonify({"error": "Brand not found"}), 404

@driver_bp.route('/drivers', methods=['POST'])
def create_driver():
    data = request.json
    if not data or 'first_name' not in data or 'phone' not in data:
        return jsonify({"error": "Fields 'first_name' and 'phone' are required"}), 400
    return jsonify(controller.create(data)), 201

@driver_bp.route('/drivers/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    data = request.json
    result = controller.update(driver_id, data)
    if result:
        return jsonify(result), 200
    return jsonify({"error": "Driver not found"}), 404

@driver_bp.route('/drivers/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    deleted_obj, error = controller.delete(driver_id)
    if error:
        status = 409 if "linked" in error else 404
        return jsonify({"error": error}), status
    return jsonify(deleted_obj), 200