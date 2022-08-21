from typing import Iterator, List

from .item import Item
from ..exceptions import ItemNotFound


class Inventory:

    _items: List[Item]

    def add(self, item: Item) -> None:
        self._items.append(item)

    def remove(self, item: Item) -> None:
        try:
            self._items.remove(item)
        except ValueError:
            raise ItemNotFound(item.name)

    def __iter__(self) -> Iterator[Item]:
        return iter(self._items)

    def __init__(self):
        self._items = list()

