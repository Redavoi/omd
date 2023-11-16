from typing import List, Dict, Any


class Pizza:
    def __init__(self, name: str, pizza_size: str, ingredients: List[str]):
        self.name = name
        self.pizza_size = pizza_size
        self.ingredients = ingredients

    def dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "pizza_size": self.pizza_size,
            "ingredients": self.ingredients
        }

    def __eq__(self, other):
        return self.name == other.name \
            and self.pizza_size == other.pizza_size \
            and self.ingredients == other.ingredients
