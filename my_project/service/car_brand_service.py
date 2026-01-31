from my_project.dao.car_brand_dao import CarBrandDAO
from my_project.domain.car_brand import CarBrand

class CarBrandService:
    def __init__(self):
        self.dao = CarBrandDAO()

    def _to_dto(self, brand):
        return {"id": brand.id, "name": brand.name}

    def get_all(self):
        return [self._to_dto(b) for b in self.dao.get_all()]
    
    def get_by_id(self, brand_id):
        brand = self.dao.get_by_id(brand_id)
        if not brand:
            return None
        return self._to_dto(brand)

    def get_brands_with_models(self):
        brands = self.dao.get_all()
        return [{
            "brand": b.name,
            "models": [m.name for m in b.models] 
        } for b in brands]
    
    def get_brand_models(self, brand_id):
        brand = self.dao.get_by_id(brand_id)
        if not brand:
            return None
        
        return {
            "brand_id": brand.id,
            "brand_name": brand.name,
            "models_list": [
                {"id": m.id, "name": m.name, "body": m.body_type} 
                for m in brand.models
            ]
        }

    def create(self, name):
        new_brand = CarBrand(name=name)
        created_brand = self.dao.create(new_brand)
        return self._to_dto(created_brand)

    def update(self, brand_id, name):
        updated_brand = self.dao.update(brand_id, name)
        if updated_brand:
            return self._to_dto(updated_brand)
        return None

    def delete(self, brand_id):
        brand = self.dao.get_by_id(brand_id)
        if not brand:
            return None, "Brand not found"
        
        dto = self._to_dto(brand)
        success = self.dao.delete(brand_id)
        
        if success:
            return dto, None
        else:
            return None, "Cannot delete brand: check related models"
        
    def get_brand_audience(self, brand_id):
        brand = self.dao.get_by_id(brand_id)
        if not brand: return None

        unique_clients = set()
        
        for model in brand.models:
            for car in model.cars:
                for order in car.orders:
                    if order.client:
                        unique_clients.add(order.client)
        
        return {
            "brand_id": brand.id,
            "brand_name": brand.name,
            "unique_clients_count": len(unique_clients),
            "clients": [
                {"id": c.id, "name": c.first_name, "phone": c.phone}
                for c in unique_clients
            ]
        }