from my_project.db import db

class Client(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    rating = db.Column(db.Numeric(3, 2), default=5.00)

    def __repr__(self):
        return f"<Client {self.first_name}>"