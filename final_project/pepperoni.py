from pizza import Pizza


class Pepperoni(Pizza):
    def __init__(self, pizza_size: str):
        super().__init__(name="Pepperoni",
                         pizza_size=pizza_size,
                         ingredients=["tomato sauce", "mozzarella", "pepperoni"])
