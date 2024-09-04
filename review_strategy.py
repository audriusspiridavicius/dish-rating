from interfaces.review import IReview
from interfaces.get_review import IReviewsStrategy
from interfaces.rating import RatingWithReview

class AllReviews(IReviewsStrategy):
    
    def get_reviews(self, ratings: list[RatingWithReview]) -> list[IReview]:
        return [rating.review for rating in ratings]
    

class PositiveReviewsOnly(IReviewsStrategy):
    def get_reviews(self, ratings: list[RatingWithReview]) -> list[IReview]:
        return [rating.review for rating in ratings if rating > 2.5]
    

class NegativeReviewsOnly(IReviewsStrategy):
    def get_reviews(self, ratings: list[RatingWithReview]) -> list[IReview]:
        return [rating.review for rating in ratings if rating <= 2.5]