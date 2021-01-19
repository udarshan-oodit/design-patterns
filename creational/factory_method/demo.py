from models.shops.capeTownPizzaShop import CapeTownPizzaShop
from models.shops.joburgPizzaShop import JoburgPizzaShop

cpt = CapeTownPizzaShop()
pizza = cpt.order_pizza('Margherita')
print(pizza)
pizza = cpt.order_pizza('Pepperoni')
print(pizza)

print('======')

jhb = JoburgPizzaShop()
pizza = jhb.order_pizza('Margherita')
print(pizza)
pizza = jhb.order_pizza('Pepperoni')
print(pizza)
