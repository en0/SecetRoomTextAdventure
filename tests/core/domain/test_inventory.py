from unittest import TestCase
from tests.builders import an
from core.exceptions import ItemNotFound


class InventoryTests(TestCase):

    def test_add_item(self):
        item = an.item.build()
        inventory = an.inventory.build()
        inventory.add(item)

    def test_remove_item_raises_not_found(self):
        item = an.item.build()
        inventory = an.inventory.build()
        with self.assertRaises(ItemNotFound):
            inventory.remove(item)

    def test_remove_item(self):
        item = an.item.with_name("item1").build()
        inventory = an.inventory.with_item(item).build()
        inventory.remove(item)

    def test_iter_items(self):
        item1 = an.item.with_name("item1").build()
        item2 = an.item.with_name("item3").build()
        item3 = an.item.with_name("item2").build()
        inventory = an.inventory.with_items(item1, item2, item3).build()
        self.assertListEqual([item1, item2, item3], list(inventory))

    def test_removed_item_is_not_in_iterator(self):
        item1 = an.item.with_name("item1").build()
        item2 = an.item.with_name("item3").build()
        item3 = an.item.with_name("item2").build()
        inventory = an.inventory.with_items(item1, item2, item3).build()

        inventory.remove(item2)
        self.assertListEqual([item1, item3], list(inventory))

