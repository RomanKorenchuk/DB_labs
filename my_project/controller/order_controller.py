from my_project.service.order_service import OrderService

class OrderController:
    def __init__(self):
        self.service = OrderService()

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, order_id):
        return self.service.get_by_id(order_id)

    def get_history(self):
        return self.service.get_client_driver_history()

    def create(self, data):
        return self.service.create(data)

    def delete(self, order_id):
        return self.service.delete(order_id)
    
    def create_smart(self, data):
        return self.service.create_smart_order(data)