from my_project.dao.car_dao import CarDAO
from my_project.domain.car import Car

class CarService:
    def __init__(self):
        self.dao = CarDAO()

    def _to_dto(self, car):
        return {
            "id": car.id,
            "plate_number": car.plate_number,
            "model": car.model.name if car.model else None,
            "driver": car.driver.first_name if car.driver else None
        }

    def get_all(self):
        return [self._to_dto(c) for c in self.dao.get_all()]
    
    def get_by_id(self, car_id):
        car = self.dao.get_by_id(car_id)
        if not car:
            return None
        return self._to_dto(car)

    def create(self, data):
        new_car = Car(
            plate_number=data['plate_number'],
            model_id=data['model_id'],
            driver_id=data['driver_id']
        )
        created = self.dao.create(new_car)
        return self._to_dto(created)

    def update(self, car_id, data):
        updated = self.dao.update(car_id, data)
        if updated:
            return self._to_dto(updated)
        return None

    def delete(self, car_id):
        car = self.dao.get_by_id(car_id)
        if not car:
            return None, "Car not found"
        
        dto = self._to_dto(car)
        success = self.dao.delete(car_id)
        if success:
            return dto, None
        return None, "Cannot delete car: linked to orders"