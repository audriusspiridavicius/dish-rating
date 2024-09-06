from dataclasses import dataclass
from interfaces.dish import IDish


class Dish(IDish):
        
    def get_price(self) -> float:
        return self.price
    
    def get_absolute_rating(self):

        number_of_records = len(self.ratings)
        
        average_ranting = 0
        
        if number_of_records > 0:
            average_ranting = sum([rating.rating for rating in self.ratings]) / number_of_records
            average_ranting = round(average_ranting, 2)
                
        return average_ranting
    
    def __str__(self) -> str:
        return f"{self.name} {self.cusine} {self.price} {self.get_absolute_rating()} {self.type}"

    