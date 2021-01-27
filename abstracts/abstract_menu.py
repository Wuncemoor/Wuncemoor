from abc import ABC, abstractmethod
from collections import UserList
from types import FunctionType
from typing import Union, List
from pygame.surface import Surface
from data_structures.gui_tools import get_surface, align_and_blit
from data_structures.menu_tools import LogicList, MenuSpecs


class AbstractMenu(LogicList, ABC):
    """Abstract class used to make a custom Menu, capable of visualizing its data to the Player by returning a
    list of Blittables to be displayed."""

    def __init__(self, data: Union[List, UserList], logic: Union[FunctionType, List[FunctionType]], specs: MenuSpecs):
        super().__init__(data, logic)
        self.specs = specs

    @abstractmethod
    def get_blittables(self) -> List:
        pass


class CanvasMenu(AbstractMenu):
    """CanvasMenus are used as a canvas base for complex menu trees. They require a background image and  may receive
    data, pointer, or submenu visualizations in the form of a list of Blittable objects to additionally display. They
     may receive additional menus to display.

     The purpose of a CanvasMenu is to ensure that there are no "trailing images". Every time the ArtistHandler renders
     the CanvasMenu, the background image should overwrite the visuals of every Blittable that was displayed during the
      previous frame."""

    def __init__(self, data, logic, specs):
        super().__init__(data, logic, specs)
        self.window = self.initialize_window()

    def initialize_window(self) -> Surface:
        return get_surface(self.specs.bg)

    def get_window_image(self) -> Surface:
        self.blit_blittables()
        return self.window

    def blit_blittables(self):
        self.window.blit(self.specs.bg, (0, 0))
        blittables = self.get_blittables()
        for blittable in blittables:
            if blittable.blit_by_alignment:
                xr, yr, xa, ya = blittable.x_ratio, blittable.y_ratio, blittable.x_offset, blittable.y_offset
                align_and_blit(self.window, blittable.image, x_ratio=xr, y_ratio=yr, x_adjust=xa, y_adjust=ya)
            else:
                self.window.blit(blittable.image, (blittable.x_offset, blittable.y_offset))

    @abstractmethod
    def get_blittables(self):
        pass
