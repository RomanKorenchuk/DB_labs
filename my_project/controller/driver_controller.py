from my_project.service.driver_service import DriverService

class DriverController:
    def __init__(self):
        self.service = DriverService()

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, driver_id):
        return self.service.get_by_id(driver_id)

    def create(self, data):
        return self.service.create(data)

    def update(self, driver_id, data):
        return self.service.update(driver_id, data)

    def delete(self, driver_id):
        return self.service.delete(driver_id)
    
    def get_available(self):
        return self.service.get_available_drivers()
    
    def create_proc(self, data):
        return self.service.create_procedure(data)