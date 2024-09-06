from abc import ABC, abstractmethod
from nutrition.nutrition_info import NutrientInfo


class NutrientInfoFormat(ABC):
    
    @abstractmethod
    def format_nutrient_info(self, nutrient_info:NutrientInfo) -> str:
        pass