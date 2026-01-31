from flask import Blueprint, jsonify, request
from sqlalchemy import text
from my_project.db import db

# url_prefix='/api/procedures'
procedure_bp = Blueprint('procedures', __name__, url_prefix='/api/procedures')

# 1. Вставка водія (INSERT Driver)
@procedure_bp.route('/insert-driver', methods=['POST'])
def insert_driver_proc():
    data = request.json
    sql = text("CALL InsertDriver(:fn, :ph, :lic)")
    try:
        db.session.execute(sql, {
            "fn": data['first_name'], 
            "ph": data['phone'], 
            "lic": data.get('license_number', 'UNKNOWN')
        })
        db.session.commit()
        return jsonify({"message": "Driver created via Stored Procedure"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# --- 2. Розумне замовлення (M:M Smart Order) ---
@procedure_bp.route('/create-order-smart', methods=['POST'])
def create_order_mm():
    data = request.json
    sql = text("CALL CreateOrderByNames(:cn, :dl, :fr, :to, :pr)")
    try:
        db.session.execute(sql, {
            "cn": data['client_name'], 
            "dl": data['driver_license'], 
            "fr": data['pickup'], 
            "to": data['destination'], 
            "pr": data['price']
        })
        db.session.commit()
        return jsonify({"message": "Order created via Procedure"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# --- 3. Генерація брендів (Loop) ---
@procedure_bp.route('/generate-brands', methods=['POST'])
def generate_brands_loop():
    try:
        db.session.execute(text("CALL InsertTenDummyBrands()"))
        db.session.commit()
        return jsonify({"message": "10 Dummy Brands Generated!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# --- 4. Статистика (Function call) ---
@procedure_bp.route('/client-stats/<int:client_id>', methods=['GET'])
def get_client_stats_proc(client_id):
    try:
        sql = text("CALL ShowClientStats(:id)")
        result = db.session.execute(sql, {"id": client_id}).mappings().first()
        if result:
            return jsonify(dict(result)), 200
        return jsonify({"message": "No data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- 5. Курсор (Dynamic Tables) ---
@procedure_bp.route('/cursor-dynamic-tables', methods=['POST'])
def cursor_dynamic():
    try:
        sql = text("CALL CopyClientsToDynamicTables()")
        result = db.session.execute(sql).mappings().first()
        db.session.commit()
        return jsonify(dict(result)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500