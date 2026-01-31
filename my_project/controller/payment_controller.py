from my_project.service.payment_service import PaymentService

class PaymentController:
    def __init__(self):
        self.service = PaymentService()

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, p_id):
        return self.service.get_by_id(p_id)

    def create(self, data):
        return self.service.create(data['name'])

    def update(self, p_id, data):
        return self.service.update(p_id, data)

    def delete(self, p_id):
        return self.service.delete(p_id)