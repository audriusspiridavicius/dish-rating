from dataclasses import dataclass, field

from nutrition.nutrient_info_format import BasicNutrientInfo, NutrientInfoFormat
from nutrition.nutrition_info import NutrientInfo
from interfaces.display_nutrient import ShowNutrientInfo
from interfaces.display_source import DisplaySource, Console

@dataclass
class Ingredient(ShowNutrientInfo):
    
    name:str
    nutrition:NutrientInfo = None 
    nutrient_info_format:NutrientInfoFormat = field(default_factory=BasicNutrientInfo)
    display:DisplaySource = field(default_factory=Console)
    
    def get_nutrition_info(self) -> dict[str, str]:
        return self.nutrition
    
    def display_nutrient_info(self) -> None:
        self.display.display(self.nutrient_info_format.format_nutrient_info(self.nutrition)) 