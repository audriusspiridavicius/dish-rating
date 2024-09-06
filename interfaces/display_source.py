from abc import ABC, abstractmethod


class DisplaySource(ABC):
    """Abstract base class for display sources."""
    
    @abstractmethod
    def display(self, data:str):
        """Display the data on the display source."""
        pass


class Console(DisplaySource):
    """Display source that displays data on the console."""
    
    def display(self, data: str):
        print(data)