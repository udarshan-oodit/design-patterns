from models.factories.modernFactory import ModernFactory
from models.factories.oldFactory import OldFactory
from models.factories.factory import Factory


class FactorySelector:

    @staticmethod
    def createFactory(factory_name: str) -> Factory:
        if factory_name == 'Old':
            return OldFactory()
        elif factory_name == 'Modern':
            return ModernFactory()
        else:
            raise Exception('Factory not found')
