from models.shops.cape_town_pizza_shop import CapeTownPizzaShop
from models.shops.joburg_pizza_shop import JoburgPizzaShop

print('=================    Cape Town Pizza Shop    =================')
cpt = CapeTownPizzaShop()

print('-> Margherita Pizza')
pizza = cpt.order_pizza('Margherita')
print(pizza)
print()


print('-> Pepperoni Pizza')
pizza = cpt.order_pizza('Pepperoni')
print(pizza)
print()

print('=================    Joburg Pizza Shop    =================')
jhb = JoburgPizzaShop()

print('-> Margherita Pizza')
pizza = jhb.order_pizza('Margherita')
print(pizza)
print()


print('-> Pepperoni Pizza')
pizza = jhb.order_pizza('Pepperoni')
print(pizza)
print()
