import abc
from models.chairs.chair import Chair
from models.tables.table import Table


class Factory(abc.ABC):

    @abc.abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abc.abstractmethod
    def create_table(self) -> Table:
        pass
