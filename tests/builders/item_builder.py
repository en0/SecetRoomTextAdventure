from typing import Set, List
from core.domain import Item


class ItemBuilder:

    _name: str
    _tags: Set[str]

    def with_name(self, name: str) -> "ItemFactory":
        self._name = name
        return self

    def with_tag(self, tag: str) -> "ItemFactory":
        self._tags.add(tag)
        return self

    def with_tags(self, *tags: List[str]) -> "ItemFactory":
        for tag in tags:
            self._tags.add(tag)
        return self

    def build(self) -> Item:
        return Item(
            name=self._name,
            tags=self._tags,
        )

    def __init__(self):
        self._name = "foo"
        self._tags = set()

