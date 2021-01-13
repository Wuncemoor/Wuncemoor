from data_structures.gui_tools import get_alpha_surface, get_text_surface, align_and_blit

"""These are the most basic (Tier 0) components used to build custom Menus. They do not inherit from any other classes. 
They can be combined with dependent and other independent primitives to make composite mixins, which perform larger 
functions."""


class MenuYesBg:
    """Sets the initial get_blittables list to [bg_image]. Contrast with MenuNoBg, which sets initial list to empty.

    Menus using this mixin require the following specs: bg_image"""
    def get_menu_bg_image(self):
        return [self.bg_image]


class MenuNoBg:
    """Sets the initial get_blittables list to empty. Contrast with MenuYesBg, which sets initial list to [bg_image].
    Menus that don't have backgrounds need to know their offsets."""

    @staticmethod
    def get_menu_bg_image():
        return []


class StaticPointerImage:
    """A mixin for making a custom menu style through multiple inheritance. Menus with this mixin will always display
    the same pointer image to the viewer, regardless of the object being pointed at or the value of self.pointer."""

    def get_pointer_image(self):
        return self.specs.pointer_image


class ModalPointerImage:
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin will display a
    different pointer image depending on various conditions such as the object being pointed at or the value of
    self.pointer. Menus using ModalPointerImage should also be frozen."""

    def get_pointer_image(self):
        return self.specs.pointer_image[self.pointer]


class FancyTextOption:
    """A mixin for making a custom menu style through multiple inheritance. FancyTextOptions display to the viewer as a
     background image with centered text on top.

      Menus using this mixin require the following specs: button_bg, font_size, font_color, font_style"""

    def get_data_obj_images(self):
        images = []
        for i in range(len(self.data)):
            images.append(self.get_option_image(i))
        return images

    def get_option_image(self, index):
        w, h = self.specs.button_bg.get_width(), self.specs.button_bg.get_height()
        surf = get_alpha_surface(w, h)
        text = get_text_surface(self.data[index], self.specs.font_size, self.specs.font_color, self.specs.font_style)
        surf.blit(self.specs.button_bg, (0, 0))
        align_and_blit(surf, text)

        return surf
