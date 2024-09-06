from abc import ABC
from dataclasses import dataclass, field
from review import Review, IReview


@dataclass
class IRating(ABC):
    
    rating:float = 0.0
    max_rating_value:float = 10.0
    min_rating_value:float = 0.0
    
    @property
    def get_rating(self) -> float:
        return self.rating
    
    @get_rating.setter
    def set_rating(self, rating_value:float) -> None:
        
        if rating_value < self.min_rating_value:
            rating_value = self.min_rating_value
        elif rating_value > self.max_rating_value:
            rating_value = self.max_rating_value
        
        self.rating = rating_value    
        

        