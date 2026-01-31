from sqlalchemy.exc import IntegrityError
from my_project.domain.client import Client
from my_project.db import db

class ClientDAO:
    def get_all(self):
        return Client.query.all()

    def get_by_id(self, client_id):
        return Client.query.get(client_id)

    def create(self, client):
        db.session.add(client)
        db.session.commit()
        return client

    def update(self, client_id, data):
        client = Client.query.get(client_id)
        if client:
            if 'first_name' in data: client.first_name = data['first_name']
            if 'phone' in data: client.phone = data['phone']
            if 'rating' in data: client.rating = data['rating']
            db.session.commit()
        return client

    def delete(self, client_id):
        client = Client.query.get(client_id)
        if not client:
            return False
        try:
            db.session.delete(client)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False