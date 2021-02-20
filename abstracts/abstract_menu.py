from abc import ABC, abstractmethod
from collections import UserList
from types import FunctionType
from typing import Union, List
from pygame.surface import Surface
from data_structures.gui_tools import get_surface, align_and_blit
from data_structures.menu_tools import LogicList, MenuSpecs


class AbstractGetBlittables(ABC):
    """Abstract mixin for an abstract Menu. This returns a list of blittables."""

    @abstractmethod
    def get_blittables(self) -> list:
        pass


class AbstractMenu(AbstractGetBlittables, LogicList, ABC):
    """Abstract class used to make a custom Menu, capable of visualizing its data to the Player by returning a
    list of Blittables to be displayed."""

    def __init__(self, data: Union[List, UserList], logic: Union[FunctionType, List[FunctionType]], specs: MenuSpecs):
        super().__init__(data, logic)
        self.specs = specs


class CanvasMenu(AbstractMenu, ABC):
    """CanvasMenus are used as a canvas base for complex menu trees. They require a background image and  may receive
    data, pointer, or submenu visualizations in the form of a list of Blittable objects to additionally display. They
     may receive additional menus to display.

     The purpose of a CanvasMenu is to ensure that there are no "trailing images". Every time the ArtistHandler renders
     the CanvasMenu, the background image should overwrite the visuals of every Blittable that was displayed during the
      previous frame."""

    def __init__(self, data, logic, specs):
        super().__init__(data, logic, specs)
        self.canvas = self.intialize_canvas()

    def intialize_canvas(self) -> Surface:
        return get_surface(self.specs.bg)

    def get_canvas_image(self) -> Surface:
        self.blit_blittables()
        return self.canvas

    def blit_blittables(self):
        self.canvas.blit(self.specs.bg, (0, 0))
        blittables = self.get_blittables()
        for blittable in blittables:
            if blittable.blit_by_alignment:
                xr, yr, xa, ya = blittable.x_ratio, blittable.y_ratio, blittable.x_offset, blittable.y_offset
                align_and_blit(self.canvas, blittable.image, x_ratio=xr, y_ratio=yr, x_adjust=xa, y_adjust=ya)
            else:
                self.canvas.blit(blittable.image, (blittable.x_offset, blittable.y_offset))

