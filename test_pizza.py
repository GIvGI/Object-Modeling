import pytest
from unittest.mock import Mock
from carte_pizzeria import CartePizzeria
from carte_pizzeria_exception import CartePizzeriaException
from pizza import Pizza
from drink import Drink
from dessert import Dessert

def test_is_empty():
    carte = CartePizzeria([])
    assert carte.is_empty() is True


def test_nb_pizzas():
    carte = CartePizzeria([])
    carte.pizzas = [Mock(), Mock(), Mock()]
    assert carte.nb_pizzas() == 3

def test_nb_drinks():
    carte = CartePizzeria([])
    carte.drinks = [Mock(), Mock()]
    assert carte.nb_drinks() == 2

def test_nb_desserts():
    carte = CartePizzeria([])
    carte.desserts = [Mock()]
    assert carte.nb_desserts() == 1

def test_add_pizza():
    carte = CartePizzeria([])
    item = Mock(spec=Pizza)
    carte.add(item)
    assert carte.pizzas == [item]

def test_add_drink():
    carte = CartePizzeria([])
    item = Mock(spec=Drink)
    carte.add(item)
    assert carte.drinks == [item]

def test_add_dessert():
    carte = CartePizzeria([])
    item = Mock(spec=Dessert)
    carte.add(item)
    assert carte.desserts == [item]    

def test_remove():
    carte = CartePizzeria([])
    item = Mock(spec=Pizza)
    carte.pizzas = [item]
    item.name = "removable"
    carte.remove("removable")
    assert len(carte.pizzas) == 0