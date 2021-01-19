from . import pizzaShop
from models.pizzas.pizza import Pizza
from models.pizzas.pepperoni import Pepperoni
from models.pizzas.margherita import Margherita


class CapeTownPizzaShop(pizzaShop.PizzaShop):
    def _create_pizza(self, pizza_name: str) -> Pizza:
        if pizza_name == 'Margherita':
            pizza = Margherita()
            print('cpt: adding spice')
            pizza.addTopping('Cape Town Spices')
            return pizza
        elif pizza_name == 'Pepperoni':
            pizza = Pepperoni()
            print('cpt: adding pepperoni')
            pizza.addTopping('extra pepperoni')
            return pizza
        else:
            raise Exception(f'Pizza {pizza_name} not found')
