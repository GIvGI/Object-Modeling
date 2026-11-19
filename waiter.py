from menu import Menu
from menu_item import MenuItem
from menu_item_iterator import MenuItemIterator
class Waiter:
    def __init__(self, menus : list[Menu]) :
        self.__menus = menus

    def displayMenus(self) -> str:
        parts: list[str] = []
        for menu in self.__menus:
            parts.append(f"{menu}\n")
        return "".join(parts)

    def displayMenuItem(self, itemName : str) -> str:
        item = self.findMenuItemFrom(itemName)
        if item is None:
            return ""
        else: 
            return str(item)

    def displayPrice(self, itemName : str) -> str:
        item = self.findMenuItemFrom(itemName)
        if item is None:
            return "0.0"
        else:
            return str(item.getPrice())

    def displayComposition(self, itemName : str) -> str:
        item = self.findMenuItemFrom(itemName)
        if item is None:
            return ""
        else:
            return item.getComposition()


    def findMenuItemFrom(self, itemName: str) -> MenuItem | None:
        if itemName is not None:
            for menu in self.__menus:
                iterator: MenuItemIterator = menu.getIterator()
                while iterator.hasNext():
                    item = iterator.next()
                    if item.getName() == itemName:
                        return item
        return None            