from abc import ABC, abstractmethod
from .review import IReview
from interfaces.rating import RatingWithReview

class IReviewsStrategy(ABC):
    
    @abstractmethod
    def get_reviews(self, ratings:list[RatingWithReview]) -> list[IReview]:
        pass
    

