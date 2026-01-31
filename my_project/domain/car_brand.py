from my_project.db import db

class CarBrand(db.Model):
    __tablename__ = 'car_brands'
    
    # Стовпці таблиці
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    # Метод для зручного відображення (не обов'язково, але корисно)
    def __repr__(self):
        return f"<Brand {self.name}>"