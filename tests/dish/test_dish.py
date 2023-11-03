from src.models.dish import Dish, Ingredient  # noqa: F401, E261, E501
import pytest

# Req 2
def test_dish():
    dish1 = Dish('Lasagna', 15.99)
    dish2 = Dish('Pasta', 12.99)

    assert dish1.name == 'Lasagna'

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Lasagna", '1599')

    with pytest.raises(ValueError, match="Dish price must be greater then zero."):
        Dish('Pasta', -1) 

    assert repr(dish1) == "Dish('Lasagna', R$15.99)"
    assert dish1 == dish1
    assert dish1 != dish2

    assert hash(dish1) == hash(repr(dish1))
    assert hash(dish1) != hash(repr(dish2))

    dish1.add_ingredient_dependency(Ingredient('queijo mussarela'), 2)
    assert dish1.recipe == {Ingredient ('queijo mussarela'): 2}
    assert dish1.get_ingredients() == set(dish1.recipe.keys())
    assert dish1.get_restrictions() == set()
