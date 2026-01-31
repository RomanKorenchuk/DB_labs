from my_project.service.car_model_service import CarModelService

class CarModelController:
    def __init__(self):
        self.service = CarModelService()

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, model_id):
        return self.service.get_by_id(model_id)

    def create(self, data):
        return self.service.create(data)

    def update(self, model_id, data):
        return self.service.update(model_id, data)

    def delete(self, model_id):
        return self.service.delete(model_id)
    
    def get_fleet(self, model_id):
        return self.service.get_model_fleet(model_id)