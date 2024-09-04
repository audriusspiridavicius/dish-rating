from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class IReview(ABC):
   
   author:str 
   review:str