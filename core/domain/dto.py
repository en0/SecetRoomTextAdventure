from typing import NamedTuple
from . import Thing, Room, Item


class ThingDTO(NamedTuple):
    name: str
    desc: str

    @staticmethod
    def from_thing(thing: Thing) -> "ThingDTO":
        return ThingDTO(
            thing.get_name(),
            thing.get_description(),
        )


class RoomDTO(NamedTuple):
    name: str
    desc: str

    @staticmethod
    def from_room(room: Room) -> "RoomDTO":
        return RoomDTO(
            room.get_name(),
            room.get_description()
        )


class ItemDTO(NamedTuple):
    name: str

    @staticmethod
    def from_item(item: Item) -> "ItemDTO":
        return ItemDTO(item.name)
