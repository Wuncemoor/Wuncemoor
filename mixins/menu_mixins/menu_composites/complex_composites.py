

"""These components (Tier 2) for building custom Menus are much larger than primitives."""
from mixins.menu_mixins.menu_composites.simple_composites import DescendingFancyTextData, DescendingStaticImagePointer, \
    LeftToRightStaticImagePointer, LeftToRightFancyTextData


class DescendingFancyButtons(DescendingFancyTextData, DescendingStaticImagePointer):
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin have their data
    displayed to the viewer from top to bottom using the "FancyText" format. When self.pointer increases, the pointer
     image will display lower on the screen to the viewer (y increases). Menus with this mixin will always display
    the same pointer image to the viewer, regardless of the object being pointed at or the value of self.pointer.

    Menus using this mixin require the following specs: button_bg, button_x_offset, button_y_offset, button_gap,
    font_size, font_color, font_style, pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""


class LeftToRightFancyButtons(LeftToRightFancyTextData, LeftToRightStaticImagePointer):
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin have their data
    displayed to the viewer from left to right using the 'FancyText' format. When self.pointer increases, the pointer
    image will display further to the right on the screen (x increases). Menus with this mixin will alwlways display the
    same pointer image to the viewer, regardless of the object being pointed at or the value of self.pointer.

    Menus using this mixin require the following specs: button_bg, button_x_offset, button_y_offset, button_gap,
    font_size, font_color, font_style, pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""
