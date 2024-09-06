from dataclasses import dataclass

@dataclass
class NutrientInfo:

    def __init__(self, nutritional_values:dict[str, str], title= "Average nutritional values per 100g") -> None:
        self.data = {"title":title, **nutritional_values} 
