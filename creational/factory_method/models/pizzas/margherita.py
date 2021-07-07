from .pizza import Pizza


class Margherita(Pizza):

    def __init__(self):
        super().__init__(sauce='tomato', cheese='cheddar')
