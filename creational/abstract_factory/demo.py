from models.factories import FactorySelector, Factory


def create_and_enjoy_furniture(factory: Factory):
    chair = factory.create_chair()
    table = factory.create_table()
    chair.sit_on()
    table.place_item('a bowl')


print('=================    Old Factory    =================')
factory = FactorySelector.create_factory(FactorySelector.OLD_STYlE)
create_and_enjoy_furniture(factory)

print()
print('=================    Modern Factory    =================')
factory = FactorySelector.create_factory(FactorySelector.MODERN_STYLE)
create_and_enjoy_furniture(factory)



