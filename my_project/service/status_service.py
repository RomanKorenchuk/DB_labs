from my_project.dao.status_dao import StatusDAO
from my_project.domain.order_status import OrderStatus

class StatusService:
    def __init__(self):
        self.dao = StatusDAO()

    def _to_dto(self, status):
        return {"id": status.id, "name": status.name}

    def get_all(self):
        return [self._to_dto(s) for s in self.dao.get_all()]
    
    def get_by_id(self, status_id):
        status = self.dao.get_by_id(status_id)
        if not status:
            return None
        return self._to_dto(status)

    def create(self, name):
        new_status = OrderStatus(name=name)
        created = self.dao.create(new_status)
        return self._to_dto(created)

    def update(self, status_id, data):
        updated = self.dao.update(status_id, data)
        if updated:
            return self._to_dto(updated)
        return None

    def delete(self, status_id):
        status = self.dao.get_by_id(status_id)
        if not status:
            return None, "Status not found"
        
        dto = self._to_dto(status)
        if self.dao.delete(status_id):
            return dto, None
        return None, "Cannot delete status: used in orders"