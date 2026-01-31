from sqlalchemy.exc import IntegrityError
from my_project.domain.order import Order
from my_project.db import db
from sqlalchemy import text

class OrderDAO:
    def get_all(self):
        return Order.query.all()

    def get_by_id(self, order_id):
        return Order.query.get(order_id)

    def create(self, order):
        db.session.add(order)
        db.session.commit()
        return order

    def update(self, order_id, data):
        order = Order.query.get(order_id)
        if order:
            if 'status_id' in data: order.status_id = data['status_id']
            if 'total_price' in data: order.total_price = data['total_price']
            db.session.commit()
        return order

    def delete(self, order_id):
        order = Order.query.get(order_id)
        if not order:
            return False
        try:
            db.session.delete(order)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False
        
    def create_mm_procedure(self, client_name, driver_lic, _from, _to, price):
        sql = text("CALL CreateOrderByNames(:cn, :dl, :fr, :to, :pr)")
        try:
            db.session.execute(sql, {
                "cn": client_name, 
                "dl": driver_lic, 
                "fr": _from, 
                "to": _to, 
                "pr": price
            })
            db.session.commit()
            return True
        except Exception as e:
            print(f"SQL ERROR: {e}")
            print(f"INPUTS: Client='{client_name}', License='{driver_lic}'")
            db.session.rollback()
            return False