from dataclasses import dataclass, field
from review import Review, IReview
from interfaces.rating import IRating

@dataclass
class RatingWithReview(IRating):
    review:IReview = field(default_factory=Review)