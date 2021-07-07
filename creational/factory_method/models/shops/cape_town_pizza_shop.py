from . import pizza_shop
from models.pizzas.pizza import Pizza
from models.pizzas.pepperoni import Pepperoni
from models.pizzas.margherita import Margherita


class CapeTownPizzaShop(pizza_shop.PizzaShop):
    def _create_pizza(self, pizza_name: str) -> Pizza:
        if pizza_name == 'Margherita':
            pizza = Margherita()
            print('cpt: adding spice')
            pizza.add_topping('Cape Town Spices')
            return pizza
        elif pizza_name == 'Pepperoni':
            pizza = Pepperoni()
            print('cpt: adding pepperoni')
            pizza.add_topping('extra pepperoni')
            return pizza
        else:
            raise Exception(f'Pizza {pizza_name} not found')
