from typing import List
from core.domain import Item, Portal, Room

from .thing_builder import ThingBuilder


class PortalBuilder(ThingBuilder[Portal]):

    _connects = None

    def with_rooms(self, room1: Room, room2: Room) -> "PortalBuilder":
        self._connects = (room1, room2)
        return self

    def _build_thing(self, name: str, items: List[Item]) -> Portal:
        if self._connects is None:
            raise ValueError("You must call with_rooms.")
        return Portal(name, items, *self._connects)
