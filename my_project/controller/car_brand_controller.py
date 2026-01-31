from my_project.service.car_brand_service import CarBrandService

class CarBrandController:
    def __init__(self):
        self.service = CarBrandService()

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, brand_id):
        return self.service.get_by_id(brand_id)

    def get_with_models(self):
        return self.service.get_brands_with_models()
    
    def get_models_by_brand(self, brand_id):
        return self.service.get_brand_models(brand_id)

    def create(self, data):
        return self.service.create(data['name'])

    def update(self, brand_id, data):
        return self.service.update(brand_id, data['name'])

    def delete(self, brand_id):
        return self.service.delete(brand_id)
    
    def get_audience(self, brand_id):
        return self.service.get_brand_audience(brand_id)