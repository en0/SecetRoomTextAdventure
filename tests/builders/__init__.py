from .inventory_builder import InventoryBuilder
from .item_builder import ItemBuilder
from .room_builder import RoomBuilder
from .table_builder import TableBuilder
from .portal_builder import PortalBuilder
from .game_interactor_builder import GameInteractorBuilder


class _An:

    @property
    def inventory(self) -> InventoryBuilder:
        return InventoryBuilder()

    @property
    def item(self) -> ItemBuilder:
        return ItemBuilder()


class _A:

    @property
    def table(self) -> TableBuilder:
        return TableBuilder()

    @property
    def portal(self) -> PortalBuilder:
        return PortalBuilder()

    @property
    def room(self) -> RoomBuilder:
        return RoomBuilder()

    @property
    def game_interactor(self) -> GameInteractorBuilder:
        return GameInteractorBuilder()


an = _An()
a = _A()

