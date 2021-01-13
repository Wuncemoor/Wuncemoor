# @dataclass
# class BasicMenuSpecs:
#
#     bg_image: Surface
#     pointer_image: Surface
#     option_bg_image = None
#     option_width:
#     option_height
#     option_delta
#     option_imagetype
#     option_direction
#     pointer_image
#     pointer_direction
#     if bg_image is not None:
#         add
#         bg_image
#         to
#         blittables
#     add
#     each
#     option
#     to
#     blittables
#     add
#     pointer
#     to
#     blittables
#
#
#
#
# class InventoryMenu(TopLevelMenu, SneakPeekMenu, LeftToRightPointer, ModalPointer, ImageMenu):
#
#     def __init__(self, data, logic, specs):
#         super.__init__(data, logic, specs)
#
# @dataclass
# class InventorySpecs:
#     bg: Surface
#     pointer_image: Surface
#     pointer_x_offset: int = 0
#     pointer_y_offset: int = 0
#     button_bg: Union[Surface, None] = None
#     button_x_offset: int = 0
#     button_y_offset: int = 0
#     button_gap: int = 0
#     font_size: int = 12
#     font_color: tuple = WHITE
#     font_style: str = 'source_sans_pro'


# class NoExtrasMixin:
#     """A mixin for making a custom menu style through multiple inheritance. This is the default ExtrasMixin to most
#     Menus that have no additional display screens or data."""
#
#     def get_extra_images(self) -> List:
#         return []


# class BacklitPointerMixin():
#     """A mixin for making a custom menu style through multiple inheritance. BacklitPointer Menus do not return a window and
#     pointer, only a window. The pointer has already been displayed within the window. Other pointers are displayed after
#     (appearing on top of) the data, usually a list of options. Backlit pointers will display after thee button
#     background, before the button data."""
#
#     def get_window_image(self):
#         self.window = self.initialize_window()
#         for index, value in enumerate(self.data):
#             if self.specs.button_bg:
#                 option = self.get_button_surface(index)
#             else:
#                 option = get_text_surface(self.data[index], self.specs.font_size, self.specs.font_color, self.specs.font_style)
#             self.window.blit(option, (self.specs.button_x_offset + self.specs.pointer_room,
#                                       self.specs.button_y_offset + (index * (option.get_height() + self.specs.button_gap))))
#
#         self.blit_pointer(option)
#         return self.window

# class MultiMenu:
#     pass
