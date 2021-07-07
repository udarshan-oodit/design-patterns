import abc
from models.pizzas.pizza import Pizza


class PizzaShop(abc.ABC):

    def order_pizza(self, pizza_name: str) -> Pizza:
        pizza = self._create_pizza(pizza_name)
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abc.abstractmethod
    def _create_pizza(self, pizza_name: str) -> Pizza:
        pass
