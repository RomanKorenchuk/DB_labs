from flask import Blueprint, jsonify, request
from my_project.controller.review_controller import ReviewController

review_bp = Blueprint('reviews', __name__)
controller = ReviewController()

@review_bp.route('/reviews', methods=['GET'])
def get_all_reviews():
    return jsonify(controller.get_all())

@review_bp.route('/drivers/<int:driver_id>/reviews', methods=['GET'])
def get_driver_reviews(driver_id):
    return jsonify(controller.get_by_driver(driver_id))

@review_bp.route('/reviews/<int:review_id>', methods=['GET'])
def get_review_by_id(review_id):
    review = controller.get_by_id(review_id)
    if review:
        return jsonify(review), 200
    return jsonify({"error": "Brand not found"}), 404

@review_bp.route('/reviews', methods=['POST'])
def create_review():
    data = request.json
    if not data or 'rating' not in data or 'order_id' not in data:
        return jsonify({"error": "Fields 'rating' and 'order_id' required"}), 400
    
    result = controller.create(data)
    if result:
        return jsonify(result), 201
    return jsonify({"error": "Order not found or already reviewed"}), 400

@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json
    res = controller.update(review_id, data)
    if res: return jsonify(res), 200
    return jsonify({"error": "Review not found"}), 404

@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    deleted, error = controller.delete(review_id)
    if error:
        return jsonify({"error": error}), 404
    return jsonify(deleted), 200