from my_project.db import db

class OrderStatus(db.Model):
    __tablename__ = 'order_statuses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    
    orders = db.relationship('Order', backref='status', lazy=True)