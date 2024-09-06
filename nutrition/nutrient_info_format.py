from interfaces.nutrient_info_format import NutrientInfoFormat
from .nutrition_info import NutrientInfo


class BasicNutrientInfo(NutrientInfoFormat):
    
    def format_nutrient_info(self, nutrient_info: NutrientInfo) -> str:
        return f"calories:{nutrient_info.data.get("calories")}\n "

    
class DetailedNutrientInfo(NutrientInfoFormat):
    
    def format_nutrient_info(self, nutrient_info: NutrientInfo) -> str:
        
        result = f"""
        
        just sample for now
        -----------------------------------------------
        calories: {nutrient_info.data.get("calories", 0.0)}
        -----------------------------------------------
        
        """
        
        return result