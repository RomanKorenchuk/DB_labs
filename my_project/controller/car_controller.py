from my_project.service.car_service import CarService

class CarController:
    def __init__(self):
        self.service = CarService()

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, car_id):
        return self.service.get_by_id(car_id)

    def create(self, data):
        return self.service.create(data)

    def update(self, car_id, data):
        return self.service.update(car_id, data)

    def delete(self, car_id):
        return self.service.delete(car_id)