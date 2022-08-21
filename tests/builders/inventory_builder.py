from typing import List
from core.domain import Inventory, Item


class InventoryBuilder:

    _items: List[Item]

    def with_item(self, item: Item) -> "InventoryBuilder":
        self._items.append(item)
        return self

    def with_items(self, *items: List[Item]) -> "InventoryBuilder":
        for item in items:
            self.with_item(item)
        return self

    def build(self) -> Inventory:
        inventory = Inventory()
        for item in self._items:
            inventory.add(item)
        return inventory

    def __init__(self):
        self._items = list()
