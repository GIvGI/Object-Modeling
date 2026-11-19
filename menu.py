from abc import ABC,abstractmethod
from menu_item_iterator import MenuItemIterator
from menu_item import MenuItem

class Menu(ABC):
    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getIterator(self) -> MenuItemIterator:
        pass

    @abstractmethod
    def addMenuItem(self,item : MenuItem) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass