from models.house import Builder


class HouseDirector:

    @staticmethod
    def buildFancyHouse():
        builder = Builder()
        builder.buildFloors(10).buildDeck().buildPool().buildGarage()
        return builder.getHouse()

    @staticmethod
    def buildApartmentBlock():
        builder = Builder()
        builder.buildFloors(100).buildPool()
        return builder.getHouse()

    @staticmethod
    def buildBasicHouse():
        builder = Builder()
        builder.buildFloors(1)
        return builder.getHouse()
