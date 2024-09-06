from abc import ABC, abstractmethod


class ShowNutrientInfo(ABC):
    
    @abstractmethod
    def display_nutrient_info(self) -> None:
        pass