import click
from pizza import Pizza
from hawaiian import Hawaiian
from margherita import Margherita
from pepperoni import Pepperoni
from utils import log


@log('Приготовили за {}с!')
def bake(pizza: Pizza) -> None:
    """Готовит пиццу

    Parameters
    ----------
    pizza : Pizza
        пицца для готовки
    """
    print(f"Baking a {pizza.name} pizza")


@log('Доставили за {}с!')
def delivery(pizza: Pizza) -> None:
    """Доставляет пиццу

    Parameters
    ----------
    pizza : Pizza
        пицца для доставки
    """
    click.echo(f"Delivering a {pizza.name} pizza")


@log('Самовывоз за {}с!')
def pickup(pizza: Pizza) -> None:
    """Самовывоз пиццы

    Parameters
    ----------
    pizza : Pizza
        пицца для самовывоза
    """
    click.echo(f"Picking up a {pizza.name} pizza")


def create_pizza(*, name: str, size: str) -> Pizza:
    """Создает пиццу

    Parameters
    ----------
    name : str
        название пиццы
    pizza_size : str
        размер пиццы
    ingredients : List[str]
        ингредиенты пиццы
    """
    if name == "Hawaiian":
        return Hawaiian(size)
    elif name == "Margherita":
        return Margherita(size)
    elif name == "Pepperoni":
        return Pepperoni(size)
    else:
        raise ValueError
