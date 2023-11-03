from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        inventory_keys = list(recipe)
        for key in inventory_keys:
            inventory_quantity = self.inventory.get(key)
            quantity = recipe.get(key)
        return inventory_quantity >= quantity

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        inventory_keys = list(recipe)
        for key in inventory_keys:
            inventory_quantity = self.inventory.get(key)
            if self.check_recipe_availability(recipe):
                self.inventory.update({key: inventory_quantity - recipe[key]})
            else:
                raise ValueError("Recipe not avaiable")
