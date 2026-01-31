from sqlalchemy.exc import IntegrityError
from my_project.domain.driver import Driver
from my_project.db import db
from sqlalchemy import text

class DriverDAO:
    def get_all(self):
        return Driver.query.all()
    
    def get_by_id(self, driver_id):
        return Driver.query.get(driver_id)

    def create(self, driver):
        db.session.add(driver)
        db.session.commit()
        return driver
    
    def update(self, driver_id, data):
        driver = Driver.query.get(driver_id)
        if driver:
            if 'first_name' in data: driver.first_name = data['first_name']
            if 'phone' in data: driver.phone = data['phone']
            if 'license_number' in data: driver.license_number = data['license_number']
            if 'is_available' in data: driver.is_available = data['is_available']
            db.session.commit()
        return driver

    def delete(self, driver_id):
        driver = Driver.query.get(driver_id)
        if not driver:
            return False
        try:
            db.session.delete(driver)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False
        
    def get_available(self):
        return Driver.query.filter_by(is_available=True).all()
    
    def create_via_procedure(self, first_name, phone, license_num):
        sql = text("CALL InsertDriver(:fn, :ph, :lic)")
        try:
            db.session.execute(sql, {"fn": first_name, "ph": phone, "lic": license_num})
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False