from sqlalchemy.exc import IntegrityError
from my_project.domain.car_brand import CarBrand
from my_project.db import db

class CarBrandDAO:
    def get_all(self):
        return CarBrand.query.all()

    def get_by_id(self, brand_id):
        return CarBrand.query.get(brand_id)

    def create(self, brand):
        db.session.add(brand)
        db.session.commit()
        return brand

    def update(self, brand_id, name):
        brand = CarBrand.query.get(brand_id)
        if brand:
            brand.name = name
            db.session.commit()
        return brand

    def delete(self, brand_id):
        brand = CarBrand.query.get(brand_id)
        if not brand:
            return False        
        try:
            db.session.delete(brand)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False