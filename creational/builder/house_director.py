from models.house import Builder


class HouseDirector:

    @staticmethod
    def build_fancy_house():
        builder = Builder()
        builder.build_floors(3).build_deck().build_pool().build_garage()
        return builder.get_house()

    @staticmethod
    def build_apartment_block():
        builder = Builder()
        builder.build_floors(100).build_pool()
        return builder.get_house()

    @staticmethod
    def build_basic_house():
        builder = Builder()
        builder.build_floors(1)
        return builder.get_house()
