from typing import Tuple, List

from .thing import Thing
from ..room import Room
from ..item import Item
from ...exceptions import UnknownRoom


class Portal(Thing):

    _connects: Tuple[Room, Room] = (None, None)

    def reveal_connected_room(self, room: Room):
        room1, room2 = self._connects
        if room1 == room:
            return room2
        elif room2 == room:
            return room1
        else:
            raise UnknownRoom()

    def __init__(self, name: str, items: List[Item], room1: Room, room2: Room) -> None:
        super().__init__(name, items)
        self._connects = (room1, room2)
