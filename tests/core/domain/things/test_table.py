from unittest import TestCase
from tests.builders import a, an
from core.exceptions import NoInteraction

from .test_thing import ThingTests


class TableTests(ThingTests, TestCase):

    def setUp(self):
        self.thing = a.table

    def test_raises_not_interactive_error(self):
        item = an.item.build()
        with self.assertRaises(NoInteraction):
            self.thing.build().interact(item)
