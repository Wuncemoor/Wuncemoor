from abc import ABC, abstractmethod
from typing import List

from data_structures.menu_tools import Blittable

"""These are the most basic components (Tier 0) used to build custom Menus. They do not inherit from any other classes 
other than ABC. Because they are abstract, they cannot be used on their own. To implement the abstract methods, a 
composite mixin must be made with the assistance of independent primitives."""


class LeftToRightPointer(ABC):
    """A mixin for making a custom menu style through multiple inheritance. When self.pointer increases, the pointer
    image will display farther right on the screen to the viewer (x increases).

    Menus with this mixin require the following specs: pointer_x_offset, pointer_y_offset, pointer_delta"""

    def get_pointer_blittable(self):
        return Blittable(image=self.get_pointer_image(),
                         x_offset=self.specs.pointer_x_offset + (self.specs.pointer_delta * self.pointer),
                         y_offset=self.specs.pointer_y_offset)

    @abstractmethod
    def get_pointer_image(self):
        pass


class DescendingPointer(ABC):
    """A mixin for making a custom menu style through multiple inheritance. When self.pointer increases, the pointer
    image will display lower on the screen to the viewer (y increases).

    Menus with this mixin require the following specs: pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""

    def get_pointer_blittable(self):
        return Blittable(image=self.get_pointer_image(),
                         x_offset=self.specs.pointer_x_offset,
                         y_offset=self.specs.pointer_y_offset + (self.specs.pointer_delta * self.pointer))

    @abstractmethod
    def get_pointer_image(self):
        pass


class AscendingPointer(ABC):
    """A mixin for making a custom menu style through multiple inheritance. When self.pointer increases, the pointer
    image will display higher on the screen to the viewer(y decreases).

    Menus with this mixin require the following specs: pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""

    def get_pointer_blittable(self):
        return Blittable(image=self.get_pointer_image(),
                         x_offset=self.specs.pointer_x_offset,
                         y_offset=self.specs.pointer_y_offset - (self.specs.pointer_delta * self.pointer))

    @abstractmethod
    def get_pointer_image(self):
        pass


class RightToLeftPointer(ABC):
    """A mixin for making a custom menu style through multiple inheritance.  When self.pointer increases, the pointer
     image will display further left on the screen to the viewer (x decreases).

     Menus with this mixin require the following specs: pointer_image, pointer_x_offset, pointer_y_offset, pointer_delta"""

    def get_pointer_blittable(self):
        return Blittable(image=self.get_pointer_image(),
                         x_offset=self.specs.pointer_x_offset - (self.specs.pointer_delta * self.pointer),
                         y_offset=self.specs.pointer_y_offset)

    @abstractmethod
    def get_pointer_image(self):
        pass


class LeftToRightData(ABC):
    """A mixin for making a custom menu style through multiple inheritance. Menus with this mixin display menu options
    to the viewer as a list from left to right.

    Menus with this mixin require the following specs: button_x_offset, button_y_offset, button_gap"""

    def get_data_blittable(self):
        img_objs = self.get_data_obj_images()
        data = []
        for ind, obj in enumerate(img_objs):
            data.append(Blittable(image=obj,
                                  x_offset=self.specs.button_x_offset + (ind * (obj.get_height() + self.specs.button_gap)),
                                  y_offset=self.specs.button_y_offset))
        return data

    @abstractmethod
    def get_data_obj_images(self):
        pass


class DescendingData(ABC):
    """A mixin for making a custom menu style through multiple inheritance. Menus with this mixin display menu options
    to the viewer as a descending list.

    Menus with this mixin require the following specs: button_x_offset, button_y_offset, button_gap"""

    def get_data_blittable(self):
        img_objs = self.get_data_obj_images()
        data = []
        for ind, obj in enumerate(img_objs):
            data.append(Blittable(image=obj, x_offset=self.specs.button_x_offset,
                                  y_offset=self.specs.button_y_offset+(ind*(obj.get_height() + self.specs.button_gap))))
        return data

    @abstractmethod
    def get_data_obj_images(self):
        pass


class AscendingData(ABC):
    """A mixin for making a custom menu style through multiple inheritance. Menus with this mixin display menu options
    to the viewer as an ascending list.

    Menus with this mixin require the following specs: button_x_offset, button_y_offset, button_gap"""

    def get_data_blittable(self):
        img_objs = self.get_data_obj_images()
        data = []
        for ind, obj in enumerate(img_objs):
            data.append(Blittable(image=obj, x_offset=self.specs.button_x_offset,
                                  y_offset=self.specs.button_y_offset+(ind*(obj.get_height() + self.specs.button_gap))))
        return data

    @abstractmethod
    def get_data_obj_images(self):
        pass


class RightToLeftData(ABC):
    """A mixin for making a custom menu style through multiple inheritance. Menus wiht this mixin display menu options
    to the viewer as a list from right to left.

    Menus with this mixin require the following specs: button_x_offset, button_y_offset, button_gap"""

    def get_data_blittable(self):
        img_objs = self.get_data_obj_images()
        data = []
        for ind, obj in enumerate(img_objs):
            data.append(Blittable(image=obj,
                                  x_offset=self.specs.button_x_offset - (ind * (obj.get_height() + self.specs.button_gap)),
                                  y_offset=self.specs.button_y_offset))
        return data

    @abstractmethod
    def get_data_obj_images(self):
        pass


class DynamicLengthModalPointerImage(ABC):
    """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin display a different
    pointer image to the viewer based on the object being pointed at."""

    def get_pointer_image(self):
        return self.get_real_pointer_image(self.pointer_data)

    @abstractmethod
    def get_real_pointer_image(self, pointer_data):
        pass


class StandardBlittables(ABC):
    """A mixin for making a custom menu style through multiple inheritance. Menus with this mixin have two blittables:
     Some data, and a pointer."""

    def get_blittables(self) -> List:
        blittables = []
        blittables.extend(self.get_data_blittable())
        blittables.append(self.get_pointer_blittable())
        return blittables

    @abstractmethod
    def get_data_blittable(self):
        pass

    @abstractmethod
    def get_pointer_blittable(self):
        pass

