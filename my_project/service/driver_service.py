from my_project.dao.driver_dao import DriverDAO
from my_project.domain.driver import Driver

class DriverService:
    def __init__(self):
        self.dao = DriverDAO()

    def _to_dto(self, driver):
        return {
            "id": driver.id, 
            "first_name": driver.first_name, 
            "phone": driver.phone,
            "license": driver.license_number,
            "status": "Free" if driver.is_available else "Busy"
        }

    def get_all(self):
        return [self._to_dto(d) for d in self.dao.get_all()]
    
    def get_by_id(self, brand_id):
        driver = self.dao.get_by_id(brand_id)
        if not driver:
            return None
        return self._to_dto(driver)

    def create(self, data):
        new_driver = Driver(
            first_name=data['first_name'],
            phone=data['phone'],
            license_number=data['license_number']
        )
        created = self.dao.create(new_driver)
        return self._to_dto(created)

    def update(self, driver_id, data):
        updated = self.dao.update(driver_id, data)
        if updated:
            return self._to_dto(updated)
        return None

    def delete(self, driver_id):
        driver = self.dao.get_by_id(driver_id)
        if not driver:
            return None, "Driver not found"
        
        dto = self._to_dto(driver)
        success = self.dao.delete(driver_id)
        if success:
            return dto, None
        return None, "Cannot delete driver: has linked cars or orders"
    
    def get_available_drivers(self):
        drivers = self.dao.get_available()
        return [self._to_dto(d) for d in drivers]
    
    def create_procedure(self, data):
        success = self.dao.create_via_procedure(
            data['first_name'], 
            data['phone'], 
            data.get('license_number', 'UNKNOWN')
        )
        if success:
            return {"message": "Driver created via Stored Procedure"}
        return None