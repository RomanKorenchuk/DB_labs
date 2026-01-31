from my_project.service.car_class_service import CarClassService

class CarClassController:
    def __init__(self):
        self.service = CarClassService()

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, class_id):
        return self.service.get_by_id(class_id)

    def get_cars(self, class_id):
        return self.service.get_class_cars(class_id)

    def create(self, data):
        return self.service.create(data)

    def update(self, class_id, data):
        return self.service.update(class_id, data)

    def delete(self, class_id):
        return self.service.delete(class_id)