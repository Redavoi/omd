from pizza import Pizza


class Pepperoni(Pizza):
    """
    Класс для представления пиццы пепперони.
    """
    def __init__(self, pizza_size: str):
        """
        Инициализирует пиццу пепперони с заданными параметрами.

        Args:
            pizza_size (str): Размер пиццы.
        """
        super().__init__(name="Pepperoni",
                         pizza_size=pizza_size,
                         ingredients=["tomato sauce",
                                      "mozzarella",
                                      "pepperoni"])
