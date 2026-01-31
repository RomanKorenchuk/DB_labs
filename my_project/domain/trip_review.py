from my_project.db import db

class TripReview(db.Model):
    __tablename__ = 'trip_reviews'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    
    order_id = db.Column(db.BigInteger, db.ForeignKey('orders.id'), unique=True, nullable=False)
    
    order = db.relationship('Order', backref=db.backref('review', uselist=False))