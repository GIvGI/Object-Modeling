from pizza import Pizza
from carte_pizzeria_exception import CartePizzeriaException

class CartePizzeria:
    def __init__(self, pizzas : list):
        self.__pizzas = pizzas

    def is_empty(self) -> bool:
        if len(self.__pizzas) == 0:
            return True
        return False

    def nb_pizzas(self) -> int:
        return len(self.__pizzas)

    def add_pizza(self, pizza : Pizza) -> None:
        self.__pizzas.append(pizza)

    def remove_pizza(self, name : str) -> None:
        found = False
        for pizza in self.__pizzas:
            if pizza.name == name:
                self.__pizzas.remove(pizza)
                found = True
                break
        if found == False:
            raise CartePizzeriaException("Pizza doesn't exist")