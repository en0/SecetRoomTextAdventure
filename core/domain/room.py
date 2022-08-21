from typing import List, Iterator

from .things import Thing
from ..exceptions import ThingNotFound


class Room:

    _name: str
    _desc: str
    _things: List[Thing]

    def get_name(self) -> str:
        return self._name

    def get_description(self):
        return self._desc

    def add(self, thing: Thing):
        self._things.append(thing)

    def remove(self, thing: Thing):
        try:
            self._things.remove(thing)
        except ValueError:
            raise ThingNotFound(thing.get_name())

    def __iter__(self) -> Iterator[Thing]:
        return iter(self._things)

    def __init__(self, name: str, desc: str):
        self._name = name
        self._desc = desc
        self._things = []
