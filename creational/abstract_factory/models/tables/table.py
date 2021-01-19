import abc


class Table(abc.ABC):

    @abc.abstractmethod
    def place_item(self, item: str):
        pass
