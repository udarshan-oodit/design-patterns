from .modern_factory import ModernFactory
from .old_factory import OldFactory
from .factory import Factory


class FactorySelector:

    OLD_STYlE = 'Old'
    MODERN_STYLE = 'Modern'

    @staticmethod
    def create_factory(factory_name: str) -> Factory:
        if factory_name == FactorySelector.OLD_STYlE:
            return OldFactory()
        elif factory_name == FactorySelector.MODERN_STYLE:
            return ModernFactory()
        else:
            raise Exception('Factory not found')
