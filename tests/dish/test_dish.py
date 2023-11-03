from src.models.dish import Dish, Ingredient  # noqa: F401, E261, E501

import pytest


# Req 2
def test_dish():
    dish1 = Dish('Batatas', 4.5)
    dish2 = Dish('Ovos', 2.5)

    assert dish1.name == 'Batatas'

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Batatas", '450')

    with pytest.raises(ValueError, match="Dish price must be greater then zero."):
        Dish('Ovos', -1) 

    assert repr(dish1) == "Dish('Batatas', R$4.50)"
    assert dish1 == dish1
    assert dish1 != dish2

    assert hash(dish1) == hash(repr(dish1))
    assert hash(dish1) != hash(repr(dish2))

    dish1.add_ingredient_dependency(Ingredient('Salt'), 100)
    assert dish1.recipe == {Ingredient ('Salt'): 100}
    assert dish1.get_ingredients() == set(dish1.recipe.keys())
    assert dish1.get_restrictions() == set()
