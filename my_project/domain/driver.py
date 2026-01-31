from my_project.db import db

class Driver(db.Model):
    __tablename__ = 'drivers'
    
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    license_number = db.Column(db.String(50), nullable=False, unique=True)
    rating = db.Column(db.Numeric(3, 2), default=5.00)
    is_available = db.Column(db.Boolean, default=True)