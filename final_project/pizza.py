from typing import List, Dict, Any


class Pizza:
    """
    Класс для представления пиццы.

    Этот класс описывает пиццу, включая её название, размер и список
    ингредиентов.
    Предоставляет методы для получения информации о пицце в виде
    словаря и сравнения с другой пиццей.

    Attributes:
        name (str): Название пиццы.
        pizza_size (str): Размер пиццы.
        ingredients (List[str]): Список ингредиентов пиццы.
    """
    def __init__(self, name: str, pizza_size: str, ingredients: List[str]):
        """
        Инициализирует новый экземпляр пиццы.

        Args:
            name (str): Название пиццы.
            pizza_size (str): Размер пиццы.
            ingredients (List[str]): Список ингредиентов.
        """
        self.name = name
        self.pizza_size = pizza_size
        self.ingredients = ingredients

    def dict(self) -> Dict[str, Any]:
        """
        Возвращает представление пиццы в виде словаря.

        Returns:
            Dict[str, Any]: Словарь с информацией о пицце.
        """
        return {
            "name": self.name,
            "pizza_size": self.pizza_size,
            "ingredients": self.ingredients
        }

    def __eq__(self, other) -> bool:
        """
        Сравнивает эту пиццу с другой на равенство.

        Args:
            other (Pizza): Другой объект пиццы для сравнения.

        Returns:
            bool: Возвращает True, если пиццы равны, иначе False.
        """
        return self.name == other.name \
            and self.pizza_size == other.pizza_size \
            and self.ingredients == other.ingredients
