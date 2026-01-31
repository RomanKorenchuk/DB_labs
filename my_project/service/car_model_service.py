from my_project.dao.car_model_dao import CarModelDAO
from my_project.domain.car_model import CarModel

class CarModelService:
    def __init__(self):
        self.dao = CarModelDAO()

    def _to_dto(self, model):
        return {
            "id": model.id, 
            "name": model.name, 
            "body_type": model.body_type,
            "brand": {
                "id": model.brand.id,
                "name": model.brand.name
            } if model.brand else None
        }

    def get_all(self):
        return [self._to_dto(m) for m in self.dao.get_all()]
    
    def get_by_id(self, model_id):
        model = self.dao.get_by_id(model_id)
        if not model:
            return None
        return self._to_dto(model)

    def create(self, data):
        new_model = CarModel(
            name=data['name'],
            body_type=data.get('body_type', 'Sedan'),
            brand_id=data['brand_id']
        )
        created = self.dao.create(new_model)
        return self._to_dto(created)

    def update(self, model_id, data):
        updated = self.dao.update(model_id, data)
        if updated:
            return self._to_dto(updated)
        return None

    def delete(self, model_id):
        model = self.dao.get_by_id(model_id)
        if not model:
            return None, "Model not found"
            
        dto = self._to_dto(model)
        success = self.dao.delete(model_id)
        
        if success:
            return dto, None
        return None, "Cannot delete model: cars are linked to it"
    
    def get_model_fleet(self, model_id):
        model = self.dao.get_by_id(model_id)
        if not model: return None

        return {
            "model_id": model.id,
            "model_name": model.name,
            "body_type": model.body_type,
            "cars_count": len(model.cars),
            "fleet": [
                {
                    "car_id": car.id,
                    "plate": car.plate_number,
                    "driver": car.driver.first_name if car.driver else "No Driver",
                    "driver_status": "Active" if car.driver and car.driver.is_available else "Busy/Off"
                }
                for car in model.cars
            ]
        }