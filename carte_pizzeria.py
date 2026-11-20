from pizza import Pizza
from dessert import Dessert
from drink import Drink
from carte_pizzeria_exception import CartePizzeriaException


class CartePizzeria:
    def __init__(self, items: list | None = None):
        self.pizzas = []
        self.drinks = []
        self.desserts = []
        if items:
            for item in items:
                self.add(item)

    def is_empty(self) -> bool:
        return len(self.pizzas) == 0 and len(self.drinks) == 0 and len(self.desserts) == 0

    def nb_pizzas(self) -> int:
        return len(self.pizzas)

    def nb_drinks(self) -> int:
        return len(self.drinks)

    def nb_desserts(self) -> int:
        return len(self.desserts)

    def add(self, item) -> None:
        if not isinstance(item, (Pizza, Drink, Dessert)):
            raise CartePizzeriaException("Unknown item type")

        for existing in self.pizzas + self.drinks + self.desserts:
            if existing.name == item.name:
                raise CartePizzeriaException("Item already exists")

        if isinstance(item, Pizza):
            for pizza in self.pizzas:
                if set(item.ingredients) == set(pizza.ingredients) and item.base == pizza.base:
                    raise CartePizzeriaException("Pizza already exists")
            self.pizzas.append(item)
        elif isinstance(item, Drink):
            self.drinks.append(item)
        else:
            self.desserts.append(item)

    def remove(self, name: str) -> None:
        for collection in (self.pizzas, self.drinks, self.desserts):
            for item in collection:
                if item.name == name:
                    collection.remove(item)
                    return

        raise CartePizzeriaException("Item doesn't exist")
