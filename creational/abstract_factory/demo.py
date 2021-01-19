from models.factories.factorySelector import FactorySelector

CUSTOMERS_CHOSEN_STYLE = 'Old'

factory = FactorySelector.createFactory(CUSTOMERS_CHOSEN_STYLE)
chair = factory.create_chair()
table = factory.create_table()
chair.sit_on()
table.place_item('test item')


CUSTOMERS_CHOSEN_STYLE = 'Modern'

factory = FactorySelector.createFactory(CUSTOMERS_CHOSEN_STYLE)
chair = factory.create_chair()
table = factory.create_table()
chair.sit_on()
table.place_item('test item')


