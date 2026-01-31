from my_project.db import db

class CarClass(db.Model):
    __tablename__ = 'car_classes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    base_rate = db.Column(db.Numeric(10, 2), nullable=False)

    cars = db.relationship('Car', backref='car_class', lazy=True)

    def __repr__(self):
        return f"<CarClass {self.name}>"