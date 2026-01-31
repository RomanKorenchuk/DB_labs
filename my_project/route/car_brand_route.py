from flask import Blueprint, jsonify, request
from my_project.controller.car_brand_controller import CarBrandController

brand_bp = Blueprint('brands', __name__)
controller = CarBrandController()

@brand_bp.route('/brands', methods=['GET'])
def get_all_brands():
    return jsonify(controller.get_all())

@brand_bp.route('/brands/extended', methods=['GET'])
def get_brands_extended():
    return jsonify(controller.get_with_models())

@brand_bp.route('/brands/<int:brand_id>', methods=['GET'])
def get_brand_by_id(brand_id):
    brand = controller.get_by_id(brand_id)
    if brand:
        return jsonify(brand), 200
    return jsonify({"error": "Brand not found"}), 404

@brand_bp.route('/brands/<int:brand_id>/models', methods=['GET'])
def get_brand_models_list(brand_id):
    data = controller.get_models_by_brand(brand_id)
    if data:
        return jsonify(data), 200
    return jsonify({"error": "Brand not found"}), 404

@brand_bp.route('/brands', methods=['POST'])
def create_brand():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Field 'name' is required"}), 400
    return jsonify(controller.create(data)), 201

@brand_bp.route('/brands/<int:brand_id>', methods=['PUT'])
def update_brand(brand_id):
    data = request.json
    result = controller.update(brand_id, data)
    if result:
        return jsonify(result), 200
    return jsonify({"error": "Brand not found"}), 404

@brand_bp.route('/brands/<int:brand_id>', methods=['DELETE'])
def delete_brand(brand_id):
    deleted_obj, error = controller.delete(brand_id)
    if error:
        status_code = 409 if "related models" in error else 404
        return jsonify({"error": error}), status_code
    return jsonify(deleted_obj), 200

@brand_bp.route('/brands/<int:brand_id>/clients', methods=['GET'])
def get_brand_clients(brand_id):
    data = controller.get_audience(brand_id)
    if data:
        return jsonify(data), 200
    return jsonify({"error": "Brand not found"}), 404
