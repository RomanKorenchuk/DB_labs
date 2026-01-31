from sqlalchemy.exc import IntegrityError
from my_project.domain.trip_review import TripReview
from my_project.db import db

class ReviewDAO:
    def get_all(self):
        return TripReview.query.all()

    def get_by_id(self, review_id):
        return TripReview.query.get(review_id)
    
    # Спеціальний метод для вибірки по водію (через JOIN)
    def get_by_driver_id(self, driver_id):
        return TripReview.query.join(TripReview.order).filter_by(driver_id=driver_id).all()

    def create(self, review):
        db.session.add(review)
        db.session.commit()
        return review

    def update(self, review_id, data):
        review = TripReview.query.get(review_id)
        if review:
            if 'rating' in data: review.rating = data['rating']
            if 'comment' in data: review.comment = data['comment']
            db.session.commit()
        return review

    def delete(self, review_id):
        review = TripReview.query.get(review_id)
        if not review: return False
        try:
            db.session.delete(review)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False