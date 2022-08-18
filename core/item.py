from typing import List, Iterable

class Item:

    name: str
    tags: List[str]

    def __init__(self, name: str, tags: Iterable[str], stackable: bool = True):
        self.name = name
        self.tags = list(tags)
