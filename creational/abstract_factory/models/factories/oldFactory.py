from models.factories.factory import Factory
from models.chairs.chair import Chair
from models.chairs.old_chair import OldChair
from models.tables.oldTable import OldTable
from models.tables.table import Table


class OldFactory(Factory):
    def create_chair(self) -> Chair:
        return OldChair()

    def create_table(self) -> Table:
        return OldTable()
