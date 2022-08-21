from unittest import TestCase
from tests.builders import a, an
from core.game_interactor import GameInteractor
from core.exceptions import ItemNotFound, ThingNotFound
from core.domain.dto import ItemDTO,ThingDTO


class GameInteractorTests(TestCase):

    def setUp(self) -> None:
        ...

    def test_create_use_command(self):
        item = an.item.build()
        inventory = an.inventory.with_item(item).build()
        table = a.table.with_name("table").build()
        room = a.room.with_thing(table).build()
        game = a.game_interactor.with_active_room(room).with_inventory(inventory).build()

        table_dto = ThingDTO.from_thing(table)
        item_dto = ItemDTO.from_item(item)
        command = game.make_use_command(table_dto, item_dto)
        self.assertIsInstance(command, GameInteractor._UseCommand)

    def test_create_use_command_raises_if_item_not_in_inventory(self):
        table = a.table.with_name("table").build()
        room = a.room.with_thing(table).build()
        game = a.game_interactor.with_active_room(room).build()

        table_dto = ThingDTO.from_thing(table)
        item_dto = ItemDTO.from_item(an.item.with_name("no-exist").build())
        with self.assertRaises(ItemNotFound):
            game.make_use_command(table_dto, item_dto)

    def test_create_use_command_raises_if_thing_not_in_active_room(self):
        item = an.item.with_name("item1").build()
        inventory = an.inventory.with_item(item).build()
        room = a.room.build()
        game = a.game_interactor.with_active_room(room).with_inventory(inventory).build()

        table_dto = ThingDTO.from_thing(a.table.with_name("no-exist").build())
        item_dto = ItemDTO.from_item(item)
        with self.assertRaises(ThingNotFound):
            game.make_use_command(table_dto, item_dto)
