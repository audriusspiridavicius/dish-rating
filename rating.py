from .interfaces.rating import IRating
from dataclasses import dataclass
from .interfaces.review import IReview
from .review import Review

@dataclass
class RatingWithReview(IRating):
    review:IReview = Review()