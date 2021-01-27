from collections import UserList
from dataclasses import dataclass
from types import FunctionType
from typing import Union, List, Tuple
from pygame.surface import Surface
from config.constants import WHITE


class TravLockList(UserList):
    """A class representing a List object with additional functionality. Has a pointer for easily accessing indexed data
     or popping from list. The list can be locked to prevent pointer movement."""

    def __init__(self, data: Union[List, UserList]):
        super().__init__(data)
        self.pointer = 0
        self.locked = False

    def traverse_list(self, amount):

        if self.locked or (amount < 0 and self.pointer == 0) or (amount > 0 and self.pointer >= (self.__len__() - 1)):
            pass
        else:
            self.pointer += amount

    @property
    def pointer_data(self):
        return self.data[self.pointer]

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def pop_pointer(self):
        pop = self.pop(self.pointer)
        if self.pointer >= len(self.data):
            self.pointer = max(0, len(self.data) - 1)
        return pop


class LogicList(TravLockList):
    """A class representing a List object with additional functionality. Has a pointer for easily accessing indexed data
     or popping from list. The list can be locked to prevent pointer movement. Also has logic attribute either as a
     FunctionType or a List of FunctionTypes."""

    def __init__(self, data: Union[List, UserList], logic: Union[FunctionType, List[FunctionType]]):
        super().__init__(data)
        self.logic = logic


@dataclass
class Blittable:
    image: Surface
    blit_by_alignment: bool = False
    x_ratio: float = 0.5
    y_ratio: float = 0.5
    x_offset: int = 0
    y_offset: int = 0


@dataclass
class MenuSpecs:
    bg: Union[Surface, Tuple]  # If no bg, must provide (width, height) to give Blittable coordinates
    pointer_image: Union[Surface, None]
    pointer_x_offset: int = 0
    pointer_y_offset: int = 0
    pointer_delta: int = 0
    button_bg: Union[Surface, None] = None
    button_x_offset: int = 0
    button_y_offset: int = 0
    button_gap: int = 0
    font_size: int = 12
    font_color: tuple = WHITE
    font_style: str = 'source_sans_pro'
