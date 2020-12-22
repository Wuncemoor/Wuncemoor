from collections import UserList
from dataclasses import dataclass
from types import FunctionType
from typing import Union, List

from pygame.surface import Surface

from config.constants import WHITE
from data_structures.gui_tools import get_alpha_surface, get_text_surface, align_and_blit

@dataclass
class MenuSpecs:
    bg: Surface
    pointer_image: Surface
    pointer_x_offset: int = 0
    pointer_y_offset: int = 0
    button_bg: Union[Surface, None] = None
    button_x_offset: int = 0
    button_y_offset: int = 0
    button_gap: int = 0
    font_size: int = 12
    font_color: tuple = WHITE
    font_style: str = 'source_sans_pro'

    @property
    def pointer_room(self):
        return int(self.pointer_image.get_width()/2)


class TravLockList(UserList):
    """A list that can be traversed and locked"""

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

    def __init__(self, data: Union[List, UserList], logic: FunctionType):
        super().__init__(data)
        self.logic = logic


class Menu(TravLockList):

    def __init__(self, data: Union[List, UserList], logic: List[FunctionType], specs: MenuSpecs):
        super().__init__(data)
        self.logic = logic
        self.specs = specs
        self.window = self.initialize_window()

    def initialize_window(self):
        window = get_alpha_surface(self.specs.bg.get_width() + self.specs.pointer_room, self.specs.bg.get_height())
        window.blit(self.specs.bg, (self.specs.pointer_room, 0))
        return window

    def blit_options(self):
        self.window = self.initialize_window()
        for index, value in enumerate(self.data):
            if self.specs.button_bg:
                option = self.get_button_surface(index)
            else:
                option = get_text_surface(self.data[index], self.specs.font_size, self.specs.font_color, self.specs.font_style)
            self.window.blit(option, (self.specs.button_x_offset + self.specs.pointer_room,
                                      self.specs.button_y_offset + (index * (option.get_height() + self.specs.button_gap))))

        self.blit_pointer(option)
        return self.window

    def get_button_surface(self, index):
        w, h = self.specs.button_bg.get_width(), self.specs.button_bg.get_height()
        surf = get_alpha_surface(w, h)
        text = get_text_surface(self.data[index], self.specs.font_size, self.specs.font_color, self.specs.font_style)
        surf.blit(self.specs.button_bg, (0, 0))
        align_and_blit(surf, text)

        return surf

    def blit_pointer(self, option):
        self.window.blit(self.specs.pointer_image, (self.specs.pointer_x_offset, self.specs.pointer_y_offset +
                                                    (self.pointer * (self.specs.button_gap + option.get_height()))))
