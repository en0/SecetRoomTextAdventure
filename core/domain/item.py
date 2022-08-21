from dataclasses import dataclass
from typing import Set


@dataclass
class Item:
    name: str
    tags: Set[str]
