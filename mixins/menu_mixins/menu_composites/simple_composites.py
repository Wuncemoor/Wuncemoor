from mixins.menu_mixins.menu_primitives.dependent_primitives import LeftToRightPointer, DescendingPointer, \
    RightToLeftPointer, AscendingPointer, LeftToRightData, DescendingData, AscendingData, RightToLeftData
from mixins.menu_mixins.menu_primitives.independent_primitives import StaticPointerImage, ModalPointerImage, \
    FancyTextOption, BasicTextOption

"""These components (Tier 1) for building custom Menus are slightly larger than primitives. Generally comprised of a 
dependent primitive being supported by an independent primitive, these simple composites are effectively "functional" 
versions of the dependent primitive."""


class LeftToRightStaticImagePointer(StaticPointerImage, LeftToRightPointer):
    """A mixin for making a custom menu style through multiple inheritance. When self.pointer increases, the pointer
    image will display farther right on the screen to the viewer (x increases). Menus with this mixin will always display
    the same pointer image to the viewer, regardless of the object being pointed at or the value of self.pointer.

    Menus with this mixin require the following specs: pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""


class DescendingStaticImagePointer(StaticPointerImage, DescendingPointer):
    """A mixin for making a custom menu style through multiple inheritance.  When self.pointer increases, the pointer
     image will display lower on the screen to the viewer (y increases). Menus with this mixin will always display
    the same pointer image to the viewer, regardless of the object being pointed at or the value of self.pointer.

     Menus with this mixin require the following specs: pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""


class RightToLeftStaticImagePointer(StaticPointerImage, RightToLeftPointer):
    """A mixin for making a custom menu style through multiple inheritance.  When self.pointer increases, the pointer
    image will display farther left on the screen to the viewer (x decreases). Menus with this mixin will always display
    the same pointer image to the viewer, regardless of the object being pointed at or the value of self.pointer.

    Menus with this mixin require the following specs: pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""


class AscendingStaticImagePointer(StaticPointerImage, AscendingPointer):
    """A mixin for making a custom menu style through multiple inheritance. When self.pointer increases, the pointer
     image will display higher on the screen to the viewer (y decreases). Menus with this mixin will always display the
     same pointer image to the viewer, regardless of the object being pointed at or the value of self.pointer

     Menus with this mixin require the following specs: pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""


class LeftToRightModalImagePointer(ModalPointerImage, LeftToRightPointer):
    """A mixin for making a custom menu style through multiple inheritance.  When self.pointer increases, the pointer
    image will display further right on the screen to the viewer (x increases). Menus with this mixin will display a
    different image to the viewer depending on the value of self.pointer. Menus using this mixin should also have their
    lists frozen.

    Menus with this mixin require the following specs: pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""


class DescendingModalImagePointer(ModalPointerImage, DescendingPointer):
    """A mixin for making a custom menu style through multiple inheritance.  When self.pointer increases, the pointer
     image will display lower on the screen to the viewer (y increases). Menus with this mixin will display a
    different image to the viewer depending on the value of self.pointer. Menus using this mixin should also have their
    lists frozen.

    Menus with this mixin require the following specs: pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""


class RightToLeftModalImagePointer(ModalPointerImage, RightToLeftPointer):
    """A mixin for making a custom menu style through multiple inheritance.  When self.pointer increases, the pointer
    image will display farther left on the screen to the viewer (x decreases). Menus with this mixin will display a
    different image to the viewer depending on the value of self.pointer. Menus using this mixin should also have their
    lists frozen.

    Menus with this mixin require the following specs: pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""


class AscendingModalImagePointer(ModalPointerImage, AscendingPointer):
    """A mixin for making a custom menu style through multiple inheritance. When self.pointer increases, the pointer
     image will display higher on the screen to the viewer (y decreases). Menus with this mixin will display a
    different image to the viewer depending on the value of self.pointer. Menus using this mixin should also have their
    lists frozen.

    Menus with this mixin require the following specs: pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""


class LeftToRightFancyTextData(FancyTextOption, LeftToRightData):
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin have their data
    displayed to the viewer from left to right using the "FancyText" format.

    Menus using this mixin require the following specs: button_bg, button_x_offset, button_y_offset, button_gap,
    font_size, font_color, font_style"""


class DescendingFancyTextData(FancyTextOption, DescendingData):
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin have their data
    displayed to the viewer from top to bottom using the "FancyText" format.

    Menus using this mixin require the following specs: button_bg, button_x_offset, button_y_offset, button_gap,
    font_size, font_color, font_style"""


class AscendingFancyTextData(FancyTextOption, AscendingData):
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin have their data
    displayed to the viewer from bottom to top using the "FancyText" format.

    Menus using this mixin require the following specs: button_bg, button_x_offset, button_y_offset, button_gap,
    font_size, font_color, font_style"""


class RightToLeftFancyTextData(FancyTextOption, RightToLeftData):
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin have their data
    displayed to the viewer from right to left using the "FancyText" format.

    Menus using this mixin require the following specs: button_bg, button_x_offset, button_y_offset, button_gap,
    font_size, font_color, font_style"""


class LeftToRightBasicTextData(BasicTextOption, LeftToRightData):
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin have their data
     displayed to the viewer from left to right using the "BasicText" format.

     Menus using this mixin require the following specs: button_x_offset, button_y_offset, button_gap, font_size,
     font_color, font_style"""


class DescendingBasicTextData(BasicTextOption, DescendingData):
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin have their data
     displayed to the viewer from top to bottom using the "BasicText" format.

     Menus using this mixin require the following specs: button_x_offset, button_y_offset, button_gap, font_size,
     font_color, font_style"""


class AscendingBasicTextData(BasicTextOption, AscendingData):
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin have their data
     displayed to the viewer from bottom to top using the "BasicText" format.

     Menus using this mixin require the following specs: button_x_offset, button_y_offset, button_gap, font_size,
     font_color, font_style"""


class RightToLeftBasicTextData(BasicTextOption, RightToLeftData):
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin have their data
     displayed to the viewer from right to left using the "BasicText" format.

     Menus using this mixin require the following specs: button_x_offset, button_y_offset, button_gap, font_size,
     font_color, font_style"""
