from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enumerations.dish_type import DishType
from rating_and_review import RatingWithReview
from .review import IReview
from .get_review import IReviewsStrategy
from review_strategy import AllReviews

@dataclass
class IDish(ABC):
    name:str = ""
    type:DishType = DishType.NONE
    price:float = 0.0
    ingredients:list = field(default_factory=list)
    cusine:str = ""
    ratings:list[RatingWithReview] = field(default_factory=list[RatingWithReview])
    recipes:list = field(default_factory=list)
    
    review_strategy:IReviewsStrategy = field(default_factory=AllReviews)
        
    @abstractmethod
    def get_rating(self):
        pass
    
    @abstractmethod
    def get_price(self):
        pass
    
    def add_recipe(self, recipe) -> None:
        self.recipes.append(recipe)
        
    def get_reviews(self) -> list[IReview]:
        return self.review_strategy.get_reviews(self.ratings)
    