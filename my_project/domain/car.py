from my_project.db import db

class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    plate_number = db.Column(db.String(20), nullable=False, unique=True)
    
    model_id = db.Column(db.Integer, db.ForeignKey('car_models.id'), nullable=False)
    driver_id = db.Column(db.BigInteger, db.ForeignKey('drivers.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('car_classes.id'), nullable=False)

    model = db.relationship('CarModel', backref='cars')
    driver = db.relationship('Driver', backref='cars')