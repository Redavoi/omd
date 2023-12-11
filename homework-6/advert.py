from colorize_mixin import ColorizeMixin
from json_traverse import JSONTraverse


class Advert(ColorizeMixin, JSONTraverse):
    repr_color_code = 33

    def __init__(self, data: dict):
        self.price = 0

        if "title" not in data:
            raise ValueError("Отсутствует поле 'title'")
        super().__init__(data)

    def __setattr__(self, name, value):
        if name == "price" and value < 0:
            raise ValueError("price must be >= 0")
        super().__setattr__(name, value)

    def __str__(self):
        return f"{self.title} | {self.price} ₽"
