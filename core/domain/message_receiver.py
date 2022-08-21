from abc import ABC, abstractmethod
from typing import List

from .dto import RoomDTO, ThingDTO, ItemDTO


class MessageReceiver(ABC):

    @abstractmethod
    def enter_room(self, room: RoomDTO, things: List[ThingDTO]):
        ...

    @abstractmethod
    def pickup_item(self, item: ItemDTO):
        ...
