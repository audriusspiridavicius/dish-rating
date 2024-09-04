from interfaces.review import IReview
from .interfaces.get_review import IReviewsStrategy
from .rating import RatingWithReview

class AllReviews(IReviewsStrategy):
    
    def get_reviews(self, ratings: list[RatingWithReview]) -> list[IReview]:
        return [rating.review for rating in ratings]
    

class PositiveReviewsOnly(IReviewsStrategy):
    def get_reviews(self, ratings: list[RatingWithReview]) -> list[IReview]:
        return super().get_reviews(ratings)
    

class NegativeReviewsOnly(IReviewsStrategy):
    def get_reviews(self, ratings: list[RatingWithReview]) -> list[IReview]:
        return super().get_reviews(ratings)