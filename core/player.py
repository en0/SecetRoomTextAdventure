from typing import List, Dict
from .exceptions import ItemNotFoundException
from .item import Item


class Player:

    inventory: List[Item]

    def add_inventory_item(self, item: Item):
        self.inventory.append(item)

    def get_inventory_item(self, item_name: str):
        filtered_items = filter(lambda item: item.name == item_name, self.inventory)
        found_item = next(filtered_items, None)
        if found_item is None:
            raise ItemNotFoundException(item_name)
        return found_item

    def remove_inventory_item(self, item: Item):
        self.inventory.remove(item)

    def __init__(self):
        self.inventory = list()
