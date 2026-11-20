from pizza import Pizza
from carte_pizzeria import CartePizzeria
from carte_pizzeria_exception import CartePizzeriaException

pizza1 = Pizza("delic",("ign1","ing2"), 10.0, "desc", "tomato")
pizza2 = Pizza("delic2",("ign1","ing2"), 8.0, "desc", "cream")
pizza3 = Pizza("delic3",("ign1","ing2"), 7.0, "desc", "tomato")
listpizza = [pizza1,pizza2,pizza3]

carte = CartePizzeria(listpizza)

print(carte.is_empty(listpizza))

print(carte.nb_pizzas())
print(carte.nb_desserts())

pizza4 = Pizza("delic",("ign1","ing2"), 10.0, "desc", "tomato")
carte.add(pizza4)
print(carte.nb_pizzas())

try:
    carte.remove("NonExistent")
except CartePizzeriaException as e:
    print(e)