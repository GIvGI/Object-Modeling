from pizza import Pizza
from dessert import Dessert
from drink import Drink
from carte_pizzeria_exception import CartePizzeriaException

class CartePizzeria:
    def __init__(self, items : list):
        self.pizzas = []
        self.drinks = []
        self.desserts = []
        for item in items:
            if isinstance(item, Pizza):
                self.pizzas.append(item)
            if isinstance(item, Drink):
                self.drinks.append(item)
            if isinstance(item, Dessert):
                self.desserts.append(item)


    def is_empty(self, items : list) -> bool:
        if len(items) == 0:
            return True
        return False

    def nb_pizzas(self) -> int:
        return len(self.pizzas)

    def nb_pizzas(self) -> int:
        return len(self.drinks)

    def nb_desserts(self) -> int:
        return len(self.desserts)

    def add(self, item) -> None:
        if isinstance(item, Pizza):
            for pizza in self.pizzas:
                if item.name == pizza.name and item.base == pizza.base:
                    raise CartePizzeriaException("Pizza already exists")
            self.pizzas.append(item)

        if isinstance(item, Drink):
            for drink in self.drinks:
                if item.name == drink.name:
                    raise CartePizzeriaException("Drink already exists")
            self.drinks.append(item)

        if isinstance(item, Dessert):
            for dessert in self.desserts:
                if item.name == dessert.name:
                    raise CartePizzeriaException("Dessert already exists")
            self.desserts.append(item)

    def remove(self, name : str) -> None:
        found = False
        for item in self.pizzas:
            if item.name == name:
                self.pizzas.remove(item)
                found = True
                break

        for item in self.drinks:
            if item.name == name:
                self.drinks.remove(item)
                found = True
                break

        for item in self.desserts:
            if item.name == name:
                self.desserts.remove(item)
                found = True
                break
            
        if found == False:
            raise CartePizzeriaException("Pizza doesn't exist")