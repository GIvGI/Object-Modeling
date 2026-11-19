from pizza import Pizza
from carte_pizzeria import CartePizzeria
from carte_pizzeria_exception import CartePizzeriaException

pizza1 = Pizza("delic",("ign1","ing2"), 10.0)
pizza2 = Pizza("delic2",("ign1","ing2"), 8.0)
pizza3 = Pizza("delic3",("ign1","ing2"), 7.0)
listpizza = [pizza1,pizza2,pizza3]

carte = CartePizzeria(listpizza)

print(carte.is_empty())

print(carte.nb_pizzas())

pizza4 = Pizza("delic",("ign1","ing2"), 10.0)
carte.add_pizza(pizza4)
print(carte.nb_pizzas())

try:
    carte.remove_pizza("NonExistent")
except CartePizzeriaException as e:
    print(e)