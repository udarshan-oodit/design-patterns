from .table import Table


class OldTable(Table):

    def place_item(self, item: str):
        print(f'You placed {item} on the old table')
