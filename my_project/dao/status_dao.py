from sqlalchemy.exc import IntegrityError
from my_project.domain.order_status import OrderStatus
from my_project.db import db

class StatusDAO:
    def get_all(self):
        return OrderStatus.query.all()

    def get_by_id(self, status_id):
        return OrderStatus.query.get(status_id)

    def create(self, status):
        db.session.add(status)
        db.session.commit()
        return status

    def update(self, status_id, data):
        status = OrderStatus.query.get(status_id)
        if status:
            if 'name' in data: status.name = data['name']
            db.session.commit()
        return status

    def delete(self, status_id):
        status = OrderStatus.query.get(status_id)
        if not status:
            return False
        try:
            db.session.delete(status)
            db.session.commit()
            return True
        except IntegrityError:
            # Не даємо видалити статус, якщо він використовується в Orders
            db.session.rollback()
            return False