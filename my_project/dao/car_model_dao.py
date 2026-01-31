from sqlalchemy.exc import IntegrityError
from my_project.domain.car_model import CarModel
from my_project.db import db

class CarModelDAO:
    def get_all(self):
        return CarModel.query.all()
    
    def get_by_id(self, model_id):
        return CarModel.query.get(model_id)

    def create(self, model):
        db.session.add(model)
        db.session.commit()
        return model
    
    def update(self, model_id, data):
        model = CarModel.query.get(model_id)
        if model:
            if 'name' in data: model.name = data['name']
            if 'body_type' in data: model.body_type = data['body_type']
            if 'brand_id' in data: model.brand_id = data['brand_id']
            db.session.commit()
        return model

    def delete(self, model_id):
        model = CarModel.query.get(model_id)
        if not model:
            return False
        try:
            db.session.delete(model)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False