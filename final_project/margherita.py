from pizza import Pizza


class Margherita(Pizza):
    """
    Класс для представления пиццы маргарита.
    """
    def __init__(self, pizza_size: str):
        """
        Инициализирует пиццу маргарита с заданными параметрами.

        Args:
            pizza_size (str): Размер пиццы.
        """
        super().__init__(name="Margherita",
                         pizza_size=pizza_size,
                         ingredients=["tomato sauce",
                                      "mozzarella",
                                      "tomatoes"])
