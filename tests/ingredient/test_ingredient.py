from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("tomate")
    ingredient2 = Ingredient("tomate")
    assert hash(ingredient1) == hash(ingredient2)

    ingredient3 = Ingredient("queijo mussarela")
    assert hash(ingredient1) != hash(ingredient3)

    assert ingredient1 == ingredient2

    assert ingredient1 != ingredient3

    assert repr(ingredient1) == "Ingredient('tomate')"

    assert ingredient1.name == "tomate"

    assert ingredient3.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
    }

    assert hash(ingredient1) == hash(Ingredient("tomate"))
