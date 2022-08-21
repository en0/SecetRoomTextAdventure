from unittest import TestCase
from tests.builders import a, an
from core.domain.dto import ItemDTO, RoomDTO, ThingDTO


class DtoTests(TestCase):

    def test_item_dto_from_item(self):
        item = an.item.with_name("item1").build()
        item_dto = ItemDTO.from_item(item)
        self.assertEquals(item_dto.name, "item1")

    def test_thing_dto_from_thing(self):
        thing = a.table.with_name("table1"). with_desc("Table 1").build()
        thing_dto = ThingDTO.from_thing(thing)
        self.assertEquals(thing_dto.name, "table1")
        self.assertEquals(thing_dto.desc, "Table 1")

    def test_room_dto_from_thing(self):
        room = a.room.with_name("room1").with_desc("Room 1").build()
        room_dto = RoomDTO.from_room(room)
        self.assertEquals(room_dto.name, "room1")
        self.assertEquals(room_dto.desc, "Room 1")

