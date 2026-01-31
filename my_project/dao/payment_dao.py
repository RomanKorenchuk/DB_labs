from sqlalchemy.exc import IntegrityError
from my_project.domain.payment_type import PaymentType
from my_project.db import db

class PaymentDAO:
    def get_all(self):
        return PaymentType.query.all()
    
    def get_by_id(self, p_id):
        return PaymentType.query.get(p_id)

    def create(self, p_type):
        db.session.add(p_type)
        db.session.commit()
        return p_type

    def update(self, p_id, data):
        p_type = PaymentType.query.get(p_id)
        if p_type:
            if 'name' in data: p_type.name = data['name']
            db.session.commit()
        return p_type

    def delete(self, p_id):
        p_type = PaymentType.query.get(p_id)
        if not p_type: return False
        try:
            db.session.delete(p_type)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False