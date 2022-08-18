from unittest import TestCase, skip
from core import Player, Item, exceptions


class PlayerTests(TestCase):

    def setUp(self):
        self.player = Player()

    def _add_inventory_item(self, name: str, tags: list = None):
        tags = tags or []
        item = Item("foo", tags)
        self.player.add_inventory_item(item)
        return item

    def test_player_inventory_basic(self):
        expected = self._add_inventory_item("foo")
        actual = self.player.get_inventory_item("foo")
        self.assertIs(expected, actual)

    def test_player_inventory_delete_raises_not_found_exception(self):
        with self.assertRaises(exceptions.ItemNotFoundException):
            self.player.get_inventory_item("foo")

    def test_player_inventory_delete(self):
        item = Item("foo", [])
        self.player.add_inventory_item(item)
        self.player.remove_inventory_item(item)
        with self.assertRaises(exceptions.ItemNotFoundException):
            self.player.get_inventory_item("foo")

