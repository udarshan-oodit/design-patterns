from .table import Table


class ModernTable(Table):

    def place_item(self, item: str):
        print(f'You placed {item} on the modern table')
