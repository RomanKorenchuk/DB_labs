from sqlalchemy.exc import IntegrityError
from my_project.domain.car_class import CarClass
from my_project.db import db

class CarClassDAO:
    def get_all(self):
        return CarClass.query.all()

    def get_by_id(self, class_id):
        return CarClass.query.get(class_id)

    def create(self, car_class):
        db.session.add(car_class)
        db.session.commit()
        return car_class

    def update(self, class_id, data):
        car_class = CarClass.query.get(class_id)
        if car_class:
            if 'name' in data: car_class.name = data['name']
            if 'base_rate' in data: car_class.base_rate = data['base_rate']
            db.session.commit()
        return car_class

    def delete(self, class_id):
        car_class = CarClass.query.get(class_id)
        if not car_class:
            return False
        try:
            db.session.delete(car_class)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False