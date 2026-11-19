from menu_item_iterator import MenuItemIterator
from menu_item import MenuItem
class MenuBonReveilIterator(MenuItemIterator):
    def __init__(self, items : list[MenuItem]):
        self.__items = items
        self.__position : int = 0

    def hasNext(self) -> bool:
        return self.__position < len(self.__items) and self.__items[self.__position] is not None

    def next(self):
        if(not self.hasNext()):
            raise ValueError("No next element exists")
        item : MenuItem = self.__items[self.__position]
        self.__position += 1
        return item