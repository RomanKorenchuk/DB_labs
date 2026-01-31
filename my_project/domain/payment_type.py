from my_project.db import db

class PaymentType(db.Model):
    __tablename__ = 'payment_types'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    
    orders = db.relationship('Order', backref='payment_type', lazy=True)