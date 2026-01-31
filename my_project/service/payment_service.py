from my_project.dao.payment_dao import PaymentDAO
from my_project.domain.payment_type import PaymentType

class PaymentService:
    def __init__(self):
        self.dao = PaymentDAO()

    def _to_dto(self, p):
        return {"id": p.id, "name": p.name}

    def get_all(self):
        return [self._to_dto(p) for p in self.dao.get_all()]
    
    def get_by_id(self, p_id):
        p = self.dao.get_by_id(p_id)
        if not p:
            return None
        return self._to_dto(p)

    def create(self, name):
        new_type = PaymentType(name=name)
        created = self.dao.create(new_type)
        return self._to_dto(created)

    def update(self, p_id, data):
        updated = self.dao.update(p_id, data)
        if updated: return self._to_dto(updated)
        return None

    def delete(self, p_id):
        obj = self.dao.get_by_id(p_id)
        if not obj: return None, "Payment type not found"
        
        dto = self._to_dto(obj)
        if self.dao.delete(p_id):
            return dto, None
        return None, "Cannot delete: used in orders"