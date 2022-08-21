from typing import List
from core.domain import Room
from core.domain.things import Thing


class RoomBuilder:

    _name: str
    _desc: str
    _things: List[Thing]

    def with_name(self, name: str) -> "RoomBuilder":
        self._name = name
        return self

    def with_desc(self, desc: str) -> "RoomBuilder":
        self._desc = desc
        return self

    def with_thing(self, thing: Thing) -> "RoomBuilder":
        self._things.append(thing)
        return self

    def with_things(self, *things: List[Thing]) -> "RoomBuilder":
        for thing in things:
            self._things.append(thing)
        return self

    def build(self) -> Room:
        room = Room(self._name, self._desc)
        for thing in self._things:
            room.add(thing)
        return room

    def __init__(self):
        self._name = "foo"
        self._desc = "the foo room."
        self._things = list()
