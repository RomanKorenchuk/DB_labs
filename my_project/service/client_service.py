from my_project.dao.client_dao import ClientDAO
from my_project.domain.client import Client
from my_project.db import db
from sqlalchemy import text

class ClientService:
    def __init__(self):
        self.dao = ClientDAO()

    def _to_dto(self, client):
        return {
            "id": client.id,
            "first_name": client.first_name,
            "phone": client.phone,
            "rating": float(client.rating)
        }

    def get_all(self):
        return [self._to_dto(c) for c in self.dao.get_all()]
    
    def get_by_id(self, client_id):
        client = self.dao.get_by_id(client_id)
        if not client:
            return None
        return self._to_dto(client)

    def create(self, data):
        new_client = Client(
            first_name=data['first_name'],
            phone=data['phone'],
            rating=data.get('rating', 5.00)
        )
        created = self.dao.create(new_client)
        return self._to_dto(created)

    def update(self, client_id, data):
        updated = self.dao.update(client_id, data)
        if updated:
            return self._to_dto(updated)
        return None

    def delete(self, client_id):
        client = self.dao.get_by_id(client_id)
        if not client:
            return None, "Client not found"
        
        dto = self._to_dto(client)
        success = self.dao.delete(client_id)
        if success:
            return dto, None
        return None, "Cannot delete client: has active orders"
  
    def get_client_stats(self, client_id):
        client = self.dao.get_by_id(client_id)
        if not client:
            return None
        orders = client.orders
        if not orders:
            return {
                "client": client.first_name,
                "total_spent": 0.0,
                "total_rides": 0,
                "status": "Newbie"
            }

        total_spent = sum(order.total_price for order in orders)
        count = len(orders)
        
        return {
            "client": client.first_name,
            "total_spent": float(total_spent),
            "total_rides": count,
            "average_check": round(float(total_spent / count), 2),
            "status": "VIP" if total_spent > 1000 else "Regular"
        }
    
    def get_sql_stats(self, client_id):
        sql = text("CALL ShowClientStats(:id)")
        result = db.session.execute(sql, {"id": client_id}).mappings().first()
        if result:
            return dict(result)
        return None

    def trigger_cursor_copy(self):
        try:
            sql = text("CALL CopyClientsToDynamicTables()")
            result = db.session.execute(sql).mappings().first()
            db.session.commit()
            return dict(result)
        except Exception as e:
            return {"error": str(e)}