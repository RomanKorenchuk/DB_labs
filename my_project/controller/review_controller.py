from my_project.service.review_service import ReviewService

class ReviewController:
    def __init__(self):
        self.service = ReviewService()

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, r_id):
        return self.service.get_by_id(r_id)
    
    def get_by_driver(self, driver_id):
        return self.service.get_reviews_for_driver(driver_id)

    def create(self, data):
        return self.service.create(data)

    def update(self, r_id, data):
        return self.service.update(r_id, data)

    def delete(self, r_id):
        return self.service.delete(r_id)