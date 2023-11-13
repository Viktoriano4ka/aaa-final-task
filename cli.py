from random import randint
import click
from pizza import Margherita, Pepperoni, Hawaiian


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """Cooks and delivers pizza"""
    bake(pizza)
    if delivery:
        deliver(pizza)
    else:
        pickup(pizza)


def log(text: str):
    """Decorator function"""
    def decorator(func):
        def wrapper(*args):
            print(text.format(randint(15, 25)))
            return text.format(randint(15, 25))
        return wrapper
    return decorator


@log('🍳 Cooked in {} minutes!')
def bake(pizza: str) -> None:
    """Cooking pizza"""


@log('🛵 Delivered in {} minutes!')
def deliver(pizza: str) -> None:
    """Delivers pizza"""


@log('🏠 Took the order in {} minutes!')
def pickup(pizza: str) -> None:
    """Pizza pickup"""


@cli.command()
def menu() -> None:
    """Displays the menu"""
    pizzas = [Margherita(), Pepperoni(), Hawaiian()]
    for pizza in pizzas:
        pizza_dict = pizza.dict()
        print(f'- {pizza_dict["name"]} {pizza_dict["icon"]}: {", ".join(pizza_dict["ingredients"])}')


if __name__ == '__main__':
    cli()
