from abc import ABC, abstractmethod

class MenuItemIterator(ABC):
    @abstractmethod
    def hasNext(self) -> bool:
        pass
    
    @abstractmethod
    def next(self):
        pass