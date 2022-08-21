from abc import ABC
from typing import List

from ..item import Item
from ...exceptions import NoInteraction


class Thing(ABC):

    _name: str
    _desc: str
    _items: List[Item]

    def interact(self, item: Item):
        raise NoInteraction()

    def reveal_items(self) -> List[Item]:
        return list(self._items)

    def get_name(self):
        return self._name

    def get_description(self):
        return self._desc

    def set_description(self, value: str):
        self._desc = value

    def __init__(self, name: str, items: List[Item]) -> None:
        self._name = name
        self._desc = ""
        self._items = list(items)
