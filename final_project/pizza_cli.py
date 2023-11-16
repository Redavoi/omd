import click
import pizza_services


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', 'delivery', default=False, is_flag=True)
@click.argument("pizza_name", type=click.Choice(["Margherita",
                                                 "Pepperoni",
                                                 "Hawaiian"]))
@click.argument("pizza_size", type=click.Choice(["L", "XL"]))
def order(pizza_name: str, pizza_size: str, delivery: bool):
    """
    Order a pizza
    """
    pizza = pizza_services.create_pizza(name=pizza_name,
                                        size=pizza_size)
    click.echo(f"You ordered a {pizza.dict()}")
    if delivery:
        pizza_services.delivery(pizza)
    else:
        pizza_services.pickup(pizza)


@cli.command()
def menu():
    """
    Show the menu
    """
    click.echo("Menu:")
    click.echo("Pizzas:")
    click.echo("1. Margherita - Available sizes: L, XL")
    click.echo("2. Pepperoni - Available sizes: L, XL")
    click.echo("3. Hawaiian - Available sizes: L, XL")
    click.echo("\nUse 'order' command to place an order.")
