from menu import Menu
from menu_item import MenuItem
from menu_item_iterator import MenuItemIterator
from menu_rapid_sandwich_iterator import MenuRapidSandwichIterator

class MenuRapidSandwich(Menu):
    def __init__(self):
        self.__name = "Carte du rapid sandwich"
        self.__items : list[MenuItem] = []

    def getName(self) -> str:
        return self.__name

    def getIterator(self) -> MenuItemIterator:
        return MenuRapidSandwichIterator(self.__items)

    def addMenuItem(self, item : MenuItem) -> None:
        if (item is None):
            raise ValueError("Arguments invalides")
        self.__items.append(item)

    def __str__(self) -> str:
        ret = self.__name + "\n"
        for item in self.__items:
            ret += f"{item}\n"
        return ret
    