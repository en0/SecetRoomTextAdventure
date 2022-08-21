from unittest.mock import Mock
from core.domain import Room, Inventory
from core.game_interactor import GameInteractor
from core.domain.message_receiver import MessageReceiver

from .room_builder import RoomBuilder
from .inventory_builder import InventoryBuilder


class GameInteractorBuilder:

    _room: Room
    _inventory: Inventory

    def with_active_room(self, room: Room) -> "GameInteractorBuilder":
        self._room = room
        return self

    def with_inventory(self, inventory: Inventory) -> "GameInteractorBuilder":
        self._inventory = inventory
        return self

    def build(self):
        receiver = Mock(spec=MessageReceiver)()
        return GameInteractor(self._room, self._inventory, receiver)

    def __init__(self):
        self._room = RoomBuilder().build()
        self._inventory = InventoryBuilder().build()
