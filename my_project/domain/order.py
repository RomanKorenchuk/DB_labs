from my_project.db import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    pickup_address = db.Column(db.String(255))
    destination_address = db.Column(db.String(255))
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)

    client_id = db.Column(db.BigInteger, db.ForeignKey('clients.id'), nullable=False)
    driver_id = db.Column(db.BigInteger, db.ForeignKey('drivers.id'))
    car_id = db.Column(db.BigInteger, db.ForeignKey('cars.id'))

    payment_id = db.Column(db.Integer, db.ForeignKey('payment_types.id'), nullable=False, default=1)
    status_id = db.Column(db.Integer, db.ForeignKey('order_statuses.id'), nullable=False, default=1)
    
    client = db.relationship('Client', backref='orders')
    driver = db.relationship('Driver', backref='orders')
    car = db.relationship('Car', backref='orders')