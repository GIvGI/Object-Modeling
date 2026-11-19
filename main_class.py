from menu_bon_reveil import MenuBonReveil
from menu_rapid_sandwich import MenuRapidSandwich
from menu_bon_reveil import MenuBonReveil
from menu_item import MenuItem
from waiter import Waiter

mrs = MenuRapidSandwich()
mrs.addMenuItem(MenuItem("Le vegetarien", "laitue, tomate, oeufs, gruyere",2.5))
mrs.addMenuItem(MenuItem("Le parisien", "jambon, emmental, cornichon, beurre", 3.0))
mrs.addMenuItem(MenuItem("L'italien", "jambon de Parme, mozzarella, tomate", 3.0))
mrs.addMenuItem(MenuItem("L'americain", "steak hache, frites", 4.5))
mrs.addMenuItem(MenuItem("Le chaud", "saucisse, bechamel, gruyere", 4.5))

mbr = MenuBonReveil()
mrs.addMenuItem(MenuItem("Reveil 1", "1 Cafe ou 1 Chocolat + 1 croissant", 2.0))
mrs.addMenuItem(MenuItem("Reveil 2", "1 Cafe ou 1 Chocolat + 1 pain au chocolat", 2.5))
mrs.addMenuItem(MenuItem("Reveil 3", "1 Cafe ou 1 Chocolat + 1 croissant + 1 tartine", 3.0))
mrs.addMenuItem(MenuItem("Reveil 4", "1 Cafe ou 1 Chocolat + 1 pain au chocolat + 1 tartine", 3.5))

w = Waiter([mbr, mrs])
print(w.displayMenus())
print("+++ Recuperation du sandwich americain")
print(w.displayMenuItem("L'americain"))
print("+++ Recuperation du reveil 3")
print(w.displayMenuItem("Reveil 3"))
print("+++ Recuperation du prix du reveil 2")
print(w.displayPrice("Reveil 2"))
print("+++ Recuperation de la composition du sandwich chaud")
print(w.displayComposition("Le chaud"))