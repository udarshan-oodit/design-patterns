class Pizza:

    def __init__(self, sauce: str, cheese: str, toppings: list = []):
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

    def __str__(self):
        return f'Pizza: [{self.sauce}, {self.cheese}, {self.toppings or "None"}]'

    def bake(self):
        print('Baking the pizza')
    
    def cut(self):
        print('Cutting the pizza')

    def box(self):
        print('Boxing the pizza')

    def add_topping(self, topping: str):
        self.toppings.append(topping)
