from unittest import TestCase
from tests.builders import a, an
from core.exceptions import NoInteraction, UnknownRoom

from .test_thing import ThingTests


class PortalTests(ThingTests, TestCase):

    def setUp(self):
        self.room1 = a.room.build()
        self.room2 = a.room.build()
        self.thing = a.portal.with_rooms(self.room1, self.room2)

    def test_raises_not_interactive_error(self):
        item = an.item.build()
        with self.assertRaises(NoInteraction):
            self.thing.build().interact(item)

    def test_get_room2_from_room1(self):
        portal = self.thing.build()
        actual = portal.reveal_connected_room(self.room1)
        self.assertIs(self.room2, actual)

    def test_get_room1_from_room2(self):
        portal = self.thing.build()
        actual = portal.reveal_connected_room(self.room2)
        self.assertIs(self.room1, actual)

    def test_get_room_raises_if_room_is_not_connected(self):
        room = a.room.build()
        portal = self.thing.build()
        with self.assertRaises(UnknownRoom):
            portal.reveal_connected_room(room)
