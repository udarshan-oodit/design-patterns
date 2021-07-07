from models.shops import CapeTownPizzaShop, JoburgPizzaShop, PizzaShop


def make_margherita_pizza(shop: PizzaShop):
    print('-> Margherita Pizza')
    pizza = shop.order_pizza('Margherita')
    print(pizza)
    print()


def make_pepperoni_pizza(shop: PizzaShop):
    print('-> Pepperoni Pizza')
    pizza = shop.order_pizza('Pepperoni')
    print(pizza)
    print()


def main():
    print('=================    Cape Town Pizza Shop    =================')
    shop = CapeTownPizzaShop()
    make_margherita_pizza(shop)
    make_pepperoni_pizza(shop)

    print('=================    Joburg Pizza Shop    =================')
    shop = JoburgPizzaShop()
    make_margherita_pizza(shop)
    make_pepperoni_pizza(shop)


if __name__ == '__main__':
    main()
