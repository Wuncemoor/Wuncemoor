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

# class LeftToRightLinked(LeftToRightData, LeftToRightPointer):
#     """A mixin for making a custom menu style through multiple inheritance."""
#     def get_blittables(self):
#         return [self.get_data_image, self.get_pointer_image]
#
#
# class DescendingLinked(DescendingData, DescendingPointer):
#     """A mixin for making a custom menu style through multiple inheritance.  Menus with this mixin display menu options
#     to the viewer as a descending list.  When the pointer number increases, the pointer image will display lower on the
#      screen (y increases)"""
#
#     def get_blittables(self):
#         blittables = []
#         blittables.extend(self.get_data_blittable())
#         blittables.append(self.get_pointer_blittable())
#         return blittables
#
#     @abstractmethod
#     def get_data_obj_images(self):
#         pass
#
# class AscendingLinked(AscendingPointer, AscendingData):
#     """A mixin for making a custom menu style through multiple inheritance."""
#     def get_blittables(self):
#         return [self.get_data_blittable, self.get_pointer_blittable]
#
# class RighttoLeftLinked(RightToLeftPointer, RightToLeftData):
#     """A mixin for making a custom menu style through multiple inheritance."""
#     def get_blittables(self):
#         return [self.get_data_blittable, self.get_pointer_blittable]
#
#
# class Backlit:
#     pass
# class FrontLit:
#     pass

# class BasicMenu(MenuYesBg, DescendingLinked, StaticPointerImage, OptionBasicText, NoExtrasMixin, AbstractMenu):
#     """An example of a custom Menu built through multiple inheritance. This menu has a background but no option background,
#      returning an image of a vertically descending list of strings and an image of a pointer."""
#
#     def get_blittables(self) -> List:
#         blittables = self.get_menu_bg_image()
#
#         blittables.append(self.get_pointer_widget)
#         blittables.append(self.get_data_widgets)
#     BG_WIDTH = 80
#     BG_HEIGHT = 24 * len(data)
#     bg = get_alpha_surface(BG_WIDTH, BG_HEIGHT)
#     bg.blit(scale(DIALOGUE_BG, (BG_WIDTH, BG_HEIGHT)), (0, 0))
#     pointer_image = get_alpha_surface(16, 16)
#     pointer_image.blit(scale(POINTER_RIGHT, (16, 16)), (0, 0))
#     specs = MenuSpecs(bg=bg,
#                       pointer_image=pointer_image,
#                       pointer_y_offset=8,
#                       font_size=16,
#                       button_x_offset=10,
#                       button_y_offset=4)
#         return AbstractMenu(data, logic, specs)
#
#
# class SneakPeekMenu(AbstractMenu, InitWindowNoBgMixin):
#     """A Menu that returns a visual image of the data being pointed to. Moving the pointer will change the image being displayed. """
#
#     def get_window_image(self):
#         entities = self.pointer.data
#         window = self.initialize_window()
#
#         y = 0
#         for entity in entities:
#             sprite = entity.images.sprite
#             text = get_text_surface(entity.name, fontsize=24, color=WHITE)
#             item = get_alpha_surface(self.specs.option_width, self.specs.option_height)
#             align_and_blit(item, sprite, x_ratio=0.15)
#             item.blit(text, (int(item.get_width() * 0.35), int(0.5 * (item.get_height() - text.get_height()))))
#             draw.line(item, DARK_GREY, (0, self.specs.option_height - 1),
#                       (int(self.specs.option_width), self.specs.option_height - 1))
#             window.blit(item, (0, y * self.specs.option_height))
#             y += 1
#
#
#
#         def display_subinv_pointer(self, subinv):
#             if self.handler.menu_type.state is MenuSubStates.BASE:
#                 pass
#             elif self.handler.menu_type.state in (MenuSubStates.SUBMENU, MenuSubStates.SELECTED_OPTIONS):
#                 subinv.blit(POINTER_RIGHT,
#                             (0, 2 + (SUBINVENTORY_OPTION_HEIGHT * self.handler.menu_type.submenu.pointer)))
#
