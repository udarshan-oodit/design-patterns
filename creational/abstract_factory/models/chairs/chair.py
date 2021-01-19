import abc


class Chair(abc.ABC):
    @abc.abstractmethod
    def has_legs(self) -> bool:
        pass

    @abc.abstractmethod
    def sit_on(self):
        pass
