from unittest import TestCase
from tests.builders import a
from core.exceptions import ThingNotFound


class RoomTests(TestCase):

    def test_room_name(self):
        expected = "Room1"
        room = a.room.with_name(expected).build()

        actual = room.get_name()
        self.assertEquals(expected, actual)

    def test_room_desc(self):
        expected = "Room1 Desc"
        room = a.room.with_desc(expected).build()

        actual = room.get_description()
        self.assertEquals(expected, actual)

    def test_add_thing_to_room(self):
        room = a.room.build()
        thing1 = a.table.build()
        room.add(thing1)

    def test_iter_things(self):
        expected = [
            a.table.with_name("table1").build(),
            a.table.with_name("table2").build(),
            a.table.with_name("table3").build(),
        ]

        room = a.room.with_things(*expected).build()
        actual = list(room)
        self.assertListEqual(expected, actual)

    def test_remove_thing(self):
        table1 = a.table.with_name("table1").build(),
        table2 = a.table.with_name("table2").build(),
        table3 = a.table.with_name("table3").build(),
        room = a.room.with_things(table1, table2, table3).build()

        room.remove(table2)
        self.assertListEqual([table1, table3], list(room))

    def test_remove_thing_raises_thing_not_found(self):
        table = a.table.build()
        room = a.room.build()
        with self.assertRaises(ThingNotFound):
            room.remove(table)
