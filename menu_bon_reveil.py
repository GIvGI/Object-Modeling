from menu import Menu
from menu_item import MenuItem
from menu_item_iterator import MenuItemIterator
from menu_bon_reveil_iterator import MenuBonReveilIterator

class MenuBonReveil(Menu):
    def __init__(self):
        self.__items : list[MenuItem] = []
        self.__name = "Carte du Bon Reveil"

    def getName(self) -> str:
        return self.__name

    def getIterator(self) -> MenuItemIterator:
        return MenuBonReveilIterator(self.__items)

    def addMenuItem(self, item: MenuItem) -> None:
        if item is None:
            raise ValueError("Arguments invalides")
        tmp: list[MenuItem | None] = [None] * (len(self.__items) + 1)
        for i in range(len(self.__items)):
            tmp[i] = self.__items[i]
        self.__items = tmp
        self.__items[len(self.__items) - 1] = item

    def __str__(self) -> str:
        ret : str = self.__name + "\n"
        for item in self.__items:
            ret += str(item) + "\n"
        return ret