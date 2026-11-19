from menu_item_iterator import MenuItemIterator
from menu_item import MenuItem

class MenuRapidSandwichIterator(MenuItemIterator):
    def __init__(self, items : list[MenuItem]):
        self.__items = items
        self.__position = 0

    def hasNext(self) -> bool:
        return self.__position < len(self.__items)

    def next(self):
        if not self.hasNext():
            raise StopIteration("No Element Exists")
        item: MenuItem = self.__items[self.__position]
        self.__position += 1
        return item