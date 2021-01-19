from .pizzaShop import PizzaShop
from models.pizzas.pizza import Pizza
from ..pizzas.margherita import Margherita
from ..pizzas.pepperoni import Pepperoni


class JoburgPizzaShop(PizzaShop):

    def _create_pizza(self, pizza_name: str) -> Pizza:
        if pizza_name == 'Margherita':
            pizza = Margherita()
            print('jhb: adding jhb cheese ')
            pizza.addTopping('Joburg extra cheese')
            return pizza
        elif pizza_name == 'Pepperoni':
            pizza = Pepperoni()
            print('jhb: adding chilli')
            pizza.addTopping('Joburg Chilli')
            return pizza
        else:
            raise Exception(f'Pizza {pizza_name} not found')
