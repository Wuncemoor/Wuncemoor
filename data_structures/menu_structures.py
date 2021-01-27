from typing import List

from abstracts.abstract_menu import CanvasMenu, AbstractMenu
from data_structures.menu_tools import MenuSpecs
from mixins.menu_mixins.menu_composites.simple_composites import DescendingFancyTextData, DescendingStaticImagePointer,\
    DescendingBasicTextData
from mixins.menu_mixins.menu_primitives.dependent_primitives import DeluxeBlittables, MultiMenuBlittables


class FancyMenu(DescendingFancyTextData, DescendingStaticImagePointer, DeluxeBlittables, CanvasMenu):
    """A custom Menu built through multiple inheritance. As a TopLevelMenu, it has a background image and it displays a
     list of Blittables on top of the background as a single image. This image is then returned to the ArtistHandler.

    FancyMenus require the following specs: bg, button_bg, button_x_offset, button_y_offset, button_gap, font_size,
    font_color, font_style, pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""

    def __init__(self, data: str, logic, specs: MenuSpecs):
        super().__init__(data, logic, specs)


class BasicMenu(DescendingBasicTextData, DescendingStaticImagePointer, DeluxeBlittables, CanvasMenu):
    """A custom Menu built through multiple inheritance.  It has a background image, displays its data to the viewer as
    descending rows of text. Does not display directly, only returns Blittables.

    BasicMenus require the following specs: bg, button_x_offset, button_y_offset, button_gap, font_size,
     font_color, font_style, pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""

    def __init__(self, data: str, logic, specs: MenuSpecs):
        super().__init__(data, logic, specs)

