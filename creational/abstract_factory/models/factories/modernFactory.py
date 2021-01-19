from models.factories.factory import Factory
from models.chairs.chair import Chair
from models.chairs.modern_chair import ModernChair
from models.tables.modernTable import ModernTable
from models.tables.table import Table


class ModernFactory(Factory):

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()
