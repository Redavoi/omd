from pizza import Pizza


class Hawaiian(Pizza):
    """
    Класс для представления гавайской пиццы.
    """
    def __init__(self, pizza_size: str):
        """
        Инициализирует гавайскую пиццу с заданными параметрами.

        Args:
            pizza_size (str): Размер пиццы.
        """
        super().__init__(name="Hawaiian",
                         pizza_size=pizza_size,
                         ingredients=["tomato sauce",
                                      "mozzarella",
                                      "chicken",
                                      "pineapples"])
