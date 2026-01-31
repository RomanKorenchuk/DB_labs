from my_project.dao.car_class_dao import CarClassDAO
from my_project.domain.car_class import CarClass

class CarClassService:
    def __init__(self):
        self.dao = CarClassDAO()

    def _to_dto(self, car_class):
        return {
            "id": car_class.id,
            "name": car_class.name,
            "base_rate": float(car_class.base_rate)
        }

    def get_all(self):
        return [self._to_dto(c) for c in self.dao.get_all()]
    
    def get_by_id(self, class_id):
        car_class = self.dao.get_by_id(class_id)
        if not car_class:
            return None
        return self._to_dto(car_class)

    def get_class_cars(self, class_id):
        car_class = self.dao.get_by_id(class_id)
        if not car_class:
            return None
        
        return {
            "class": car_class.name,
            "base_rate": float(car_class.base_rate),
            "cars": [
                {
                    "id": car.id, 
                    "plate": car.plate_number, 
                    "model": car.model.name
                } 
                for car in car_class.cars
            ]
        }

    def create(self, data):
        new_class = CarClass(
            name=data['name'],
            base_rate=data['base_rate']
        )
        created = self.dao.create(new_class)
        return self._to_dto(created)

    def update(self, class_id, data):
        updated = self.dao.update(class_id, data)
        if updated:
            return self._to_dto(updated)
        return None

    def delete(self, class_id):
        obj = self.dao.get_by_id(class_id)
        if not obj:
            return None, "Class not found"
        
        dto = self._to_dto(obj)
        success = self.dao.delete(class_id)
        if success:
            return dto, None
        return None, "Cannot delete class: cars are linked to it"