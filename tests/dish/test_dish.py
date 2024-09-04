import pytest
from dish import Dish
from enumerations.dish_type import DishType
from rating_and_review import RatingWithReview
from review import Review
from review_strategy import AllReviews, PositiveReviewsOnly, NegativeReviewsOnly
from interfaces.dish import IDish

@pytest.fixture
def low_rating():
    return RatingWithReview(review=Review("low rating", "poor quality!"), _rating=2.3)

@pytest.fixture
def good_rating():
    return RatingWithReview(review=Review("good rating", "amazing product quality!"), _rating=9.5)

@pytest.fixture
def avarage_rating():
    return RatingWithReview(review=Review("avarage rating", "avarage quality!"), _rating=6.5)


@pytest.fixture
def ratings(good_rating, avarage_rating, low_rating):
    
    return [good_rating, good_rating, avarage_rating, low_rating]


@pytest.fixture
def dish(ratings):
    return Dish("Pasta", DishType.PASTA, ratings=ratings)


class TestDishGetPrice:
    
    
    @pytest.mark.parametrize("name, type, ingredients, cusine", [
        ("beef steak", DishType.MEAT, ["beef"], "USA"),
        ("italian delicious pasta", DishType.PASTA, ["pasta", "pasta"], "Italy"),
        ])

    def test_price_zero(self, name, type, ingredients, cusine):
        dish = Dish(name=name, cusine=cusine, type=type, ingredients=ingredients)
        
        assert dish.get_price() == 0

        
class TestDishGetReviews:
    
    def test_get_all_reviews(self, dish:IDish):
        dish.review_strategy = AllReviews()
        
        reviews = dish.get_reviews()
        
        number_of_reviews = len(reviews)
        
        assert number_of_reviews == 4
        
    
    def test_get_only_positive_reviews(self, dish):
        dish.review_strategy = PositiveReviewsOnly()
        
        reviews = dish.get_reviews()
        
        number_of_reviews = len(reviews)
        
        assert number_of_reviews == 3
    
    def test_get_only_negative_reviews(self, dish):
        dish.review_strategy = NegativeReviewsOnly()
        
        reviews = dish.get_reviews()
        
        number_of_reviews = len(reviews)
        
        assert number_of_reviews == 1