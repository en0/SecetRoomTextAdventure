from typing import List
from core.domain import Table, Item

from .thing_builder import ThingBuilder


class TableBuilder(ThingBuilder[Table]):

    def _build_thing(self, name: str, items: List[Item]) -> Table:
        return Table(name, items)
