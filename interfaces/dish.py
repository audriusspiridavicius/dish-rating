from abc import ABC, abstractmethod
from dataclasses import dataclass
from enumerations.dish_type import DishType
from .rating import IDishRating
from .review import IReview
from .get_review import IReviewsStrategy
from review_strategy import AllReviews

dataclass
class IDish(ABC):
    name:str = ""
    type:DishType = DishType.NONE
    price:float = 0.0
    ingredients = []
    cusine:str = ""
    ratings:list[IDishRating] = []
    recipes:list = []
    
    review_strategy:IReviewsStrategy = AllReviews()
        
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
    