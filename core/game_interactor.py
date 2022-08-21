from .command import Command
from .domain import Item, Room, Inventory
from .domain.things import Thing
from .domain.dto import ThingDTO, ItemDTO
from .domain.message_receiver import MessageReceiver
from .exceptions import ItemNotFound, ThingNotFound


class GameInteractor:

    class _UseCommand(Command):

        def execute(self):
            ...

        def __init__(self, game: "GameInteractor", thing: Thing, item: Item):
            self._game = game
            self._thing = thing
            self._item = item

    def make_use_command(self, thing: ThingDTO, using_item: ItemDTO) -> Command:
        item = self._find_item(using_item.name)
        thing = self._find_thing(thing.name)
        return GameInteractor._UseCommand(self, thing, item)

    def _find_item(self, item_name: str) -> Item:
        for item in self._inventory:
            if item.name == item_name:
                return item
        raise ItemNotFound(item_name)

    def _find_thing(self, thing_name: str) -> Thing:
        for thing in self._active_room:
            if thing.get_name() == thing_name:
                return thing
        raise ThingNotFound(thing_name)

    def __init__(self, initial_room: Room, inventory: Inventory, receiver: MessageReceiver):
        self._initial_room = initial_room
        self._active_room = self._initial_room
        self._inventory = inventory
        self._receiver = receiver
