from ..factories import Factory
from ..chairs import Chair, ModernChair
from ..tables import ModernTable, Table


class ModernFactory(Factory):

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()
