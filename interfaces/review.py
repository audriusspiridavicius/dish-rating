from abc import ABC
from dataclasses import dataclass

@dataclass
class IReview(ABC):
   
   author:str = ""
   review:str = ""