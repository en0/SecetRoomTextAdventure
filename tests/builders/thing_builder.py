from abc import abstractmethod
from typing import List, Generic, TypeVar
from core.domain import Item
from core.domain.things.thing import Thing

T = TypeVar("T", bound=Thing)


class ThingBuilder(Generic[T]):

    _items: List[Item]
    _name: str
    _desc: str

    def with_name(self, name: str) -> "ThingBuilder":
        self._name = name
        return self

    def with_desc(self, desc: str) -> "ThingBuilder":
        self._desc = desc
        return self

    def with_item(self, item: Item) -> "ThingBuilder":
        self._items.append(item)
        return self

    def with_items(self, *items: List[Item]) -> "ThingBuilder":
        for item in items:
            self._items.append(item)
        return self

    @abstractmethod
    def _build_thing(self, name: str, items: List[Item]) -> T:
        raise NotImplementedError()

    def build(self) -> T:
        thing = self._build_thing(self._name, self._items)
        thing.set_description(self._desc)
        return thing

    def __init__(self):
        self._name = "Foo"
        self._desc = "Foo bar baz"
        self._items = list()
