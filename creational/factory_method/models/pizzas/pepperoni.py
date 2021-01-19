from .pizza import Pizza


class Pepperoni(Pizza):

    def __init__(self):
        super().__init__('tomato', 'cheddar', ['pepponi'])
