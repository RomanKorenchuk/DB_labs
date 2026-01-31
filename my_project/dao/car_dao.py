from sqlalchemy.exc import IntegrityError
from my_project.domain.car import Car
from my_project.db import db

class CarDAO:
    def get_all(self):
        return Car.query.all()

    def get_by_id(self, car_id):
        return Car.query.get(car_id)

    def create(self, car):
        db.session.add(car)
        db.session.commit()
        return car

    def update(self, car_id, data):
        car = Car.query.get(car_id)
        if car:
            if 'plate_number' in data: car.plate_number = data['plate_number']
            if 'model_id' in data: car.model_id = data['model_id']
            if 'driver_id' in data: car.driver_id = data['driver_id']
            # class_id поки ігноруємо або додаємо за потреби
            db.session.commit()
        return car

    def delete(self, car_id):
        car = Car.query.get(car_id)
        if not car:
            return False
        try:
            db.session.delete(car)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False