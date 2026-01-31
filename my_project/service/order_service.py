from my_project.dao.order_dao import OrderDAO
from my_project.dao.client_dao import ClientDAO
from my_project.domain.order import Order

class OrderService:
    def __init__(self):
        self.dao = OrderDAO()
        self.client_dao = ClientDAO()

    def _to_dto(self, order):
        return {
            "id": order.id,
            "price": float(order.total_price),
            "date": str(order.order_date),
            
            "client": {
                "id": order.client.id,
                "name": order.client.first_name,
                "phone": order.client.phone
            } if order.client else None,

            "driver": {
                "id": order.driver.id,
                "name": order.driver.first_name,
                "license": order.driver.license_number
            } if order.driver else "Searching...",

            "car": {
                "plate": order.car.plate_number,
                "model": order.car.model.name
            } if order.car else None,
            "status": order.status.name if order.status else "Unknown",
            "payment_type": order.payment_type.name if order.payment_type else "Cash"
        }

    def get_all(self):
        return [self._to_dto(o) for o in self.dao.get_all()]
    
    def get_by_id(self, order_id):
        order = self.dao.get_by_id(order_id)
        if not order:
            return None
        return self._to_dto(order)

    def get_client_driver_history(self):
        clients = self.client_dao.get_all()
        result = []
        
        for client in clients:
            unique_drivers = {order.driver for order in client.orders if order.driver}
            
            result.append({
                "client_name": client.first_name,
                "interacted_with_drivers": [
                    {"id": d.id, "name": d.first_name, "license": d.license_number} 
                    for d in unique_drivers
                ]
            })
        return result

    def create(self, data):
        new_order = Order(
            client_id=data['client_id'],
            driver_id=data.get('driver_id'),
            car_id=data.get('car_id'),
            pickup_address=data['pickup_address'],
            destination_address=data['destination_address'],
            total_price=data['total_price'],
            payment_id=data.get('payment_id', 1),
            status_id=data.get('status_id', 1)
        )
        created = self.dao.create(new_order)
        return self._to_dto(created)

    def delete(self, order_id):
        order = self.dao.get_by_id(order_id)
        if not order:
            return None, "Order not found"
        
        dto = self._to_dto(order)
        success = self.dao.delete(order_id)
        if success:
            return dto, None
        return None, "Cannot delete order"
    
    def create_smart_order(self, data):
        success = self.dao.create_mm_procedure(
            data['client_name'],
            data['driver_license'],
            data['pickup'],
            data['destination'],
            data['price']
        )
        if success:
            return {"message": "Order created via Smart M:M Procedure"}
        return None