import pytest
from unittest.mock import Mock
from carte_pizzeria import CartePizzeria
from carte_pizzeria_exception import CartePizzeriaException
from pizza import Pizza

def test_is_empty():
    carte = CartePizzeria([])
    assert carte.is_empty() is True

def test_num_is_zero():
    carte = CartePizzeria([])
    assert carte.nb_pizzas() == 0

def test_add_pizza():
    carte = CartePizzeria([])
    pizza4 = Mock()
    carte.add_pizza(pizza4)
    assert carte._CartePizzeria__pizzas == [pizza4]

def test_remove_pizza():
    pizza4 = Mock()
    pizza4.name = "delic"
    carte = CartePizzeria([pizza4])
#hii
    carte.remove_pizza("delic")

    assert carte._CartePizzeria__pizzas == []