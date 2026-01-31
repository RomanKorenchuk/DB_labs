from my_project.dao.review_dao import ReviewDAO
from my_project.domain.trip_review import TripReview

class ReviewService:
    def __init__(self):
        self.dao = ReviewDAO()

    def _to_dto(self, review):
        return {
            "id": review.id,
            "rating": review.rating,
            "comment": review.comment,
            "order_id": review.order_id,
            "client": review.order.client.first_name if review.order.client else "Unknown"
        }

    def get_all(self):
        return [self._to_dto(r) for r in self.dao.get_all()]
    
    def get_by_id(self, review_id):
        r = self.dao.get_by_id(review_id)
        if not r:
            return None
        return self._to_dto(r)

    def get_reviews_for_driver(self, driver_id):
        reviews = self.dao.get_by_driver_id(driver_id)
        return [{
            "rating": r.rating,
            "comment": r.comment,
            "date": str(r.order.order_date),
            "client_name": r.order.client.first_name
        } for r in reviews]

    def create(self, data):
        new_review = TripReview(
            order_id=data['order_id'],
            rating=data['rating'],
            comment=data.get('comment', '')
        )
        try:
            created = self.dao.create(new_review)
            return self._to_dto(created)
        except Exception as e:
            return None

    def update(self, review_id, data):
        updated = self.dao.update(review_id, data)
        if updated: return self._to_dto(updated)
        return None

    def delete(self, review_id):
        obj = self.dao.get_by_id(review_id)
        if not obj: return None, "Review not found"
        
        dto = self._to_dto(obj)
        if self.dao.delete(review_id):
            return dto, None
        return None, "Delete failed"