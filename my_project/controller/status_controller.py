from my_project.service.status_service import StatusService

class StatusController:
    def __init__(self):
        self.service = StatusService()

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, status_id):
        return self.service.get_by_id(status_id)

    def create(self, data):
        return self.service.create(data['name'])

    def update(self, status_id, data):
        return self.service.update(status_id, data)

    def delete(self, status_id):
        return self.service.delete(status_id)