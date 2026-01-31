from my_project.db import db

class CarModel(db.Model):
    __tablename__ = 'car_models'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    body_type = db.Column(db.String(30), default='Sedan')
    
    # Зв'язок з таблицею брендів (Foreign Key)
    brand_id = db.Column(db.Integer, db.ForeignKey('car_brands.id'), nullable=False)
    
    # Це дозволить отримати об'єкт бренду через model.brand
    brand = db.relationship('CarBrand', backref='models')

    def __repr__(self):
        return f"<Model {self.name}>"