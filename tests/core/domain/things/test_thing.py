from tests.builders import a, an
from tests.builders.thing_builder import ThingBuilder


class ThingTests:

    thing: ThingBuilder

    def test_reveal_items(self):
        item1 = an.item.with_name("item1").build()
        item2 = an.item.with_name("item2").build()
        item3 = an.item.with_name("item3").build()
        thing = self.thing.with_items(item1, item2, item3).build()

        items = thing.reveal_items()
        self.assertListEqual([item1, item2, item3], items)

    def test_thing_name(self):
        thing = self.thing.with_name("thing").build()
        self.assertEquals(thing.get_name(), "thing")

    def test_thing_description(self):
        thing = self.thing.with_desc("ain't no thang.").build()
        self.assertEquals(thing.get_description(), "ain't no thang.")

