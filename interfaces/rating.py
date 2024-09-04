from abc import ABC
from dataclasses import dataclass, field
from review import Review, IReview


@dataclass
class IRating(ABC):
    
    _rating:float = 0.0
    max_rating_value:float = 10.0
    min_rating_value:float = 0.0
    
    @property
    def rating(self) -> float:
        return self._rating
    
    
    def set_rating(self, rating_value:float) -> None:
        
        if rating_value < self.min_rating_value:
            rating_value = self.min_rating_value
        elif rating_value > self.max_rating_value:
            rating_value = self.max_rating_value
        
        self._rating = rating_value    
        
@dataclass
class RatingWithReview(IRating):
    review:IReview = field(default_factory=Review)
        
@dataclass    
class IDishRating(RatingWithReview):
    pass

