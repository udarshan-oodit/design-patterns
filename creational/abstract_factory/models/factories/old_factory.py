from ..factories import Factory
from ..chairs import Chair, OldChair
from ..tables import OldTable, Table


class OldFactory(Factory):
    def create_chair(self) -> Chair:
        return OldChair()

    def create_table(self) -> Table:
        return OldTable()
