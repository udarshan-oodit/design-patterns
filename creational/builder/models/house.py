class House:

    def __init__(self, builder):
        self.floors = builder.floors
        self.has_garage = builder.has_garage
        self.has_swimming_pool = builder.has_swimming_pool
        self.has_deck = builder.has_deck

    def __str__(self):
        return f'Floors: {self.floors}, Garage: {self.has_garage}, ' \
               f'Pool: {self.has_swimming_pool}, Deck: {self.has_deck}'


class Builder:

    def __init__(self):
        self.floors = 1
        self.has_garage = False
        self.has_swimming_pool = False
        self.has_deck = False

    def buildFloors(self, num_floors):
        self.floors = num_floors
        return self

    def buildGarage(self):
        self.has_garage = True
        return self

    def buildPool(self):
        self.has_garage = True
        return self

    def buildDeck(self):
        self.has_deck = True
        return self

    def getHouse(self):
        house = House(self)
        self = Builder()
        return house
