
from config.image_objects import TITLE_MENU_BG, TITLE_MENU_BUTTON, TITLE_SCREEN_BG, POINTER_RIGHT
from data_structures.gui_tools import get_text_surface, align_and_blit
from data_structures.menu_tools import Menu, MenuSpecs
from handlers.logic.logic_chunks import new_game, load_game, goto_settings, goto_acknowledgements, quit_game


def get_title_text():
    text = get_text_surface('WUNCEMOOR', fontsize=150, style='lunchds')
    subtext = get_text_surface('THE ETERNAL DREAM', fontsize=60, style='lunchds')

    return text, subtext


def get_title_menu_specs():
    specs = MenuSpecs(bg=TITLE_MENU_BG, pointer_image=POINTER_RIGHT, pointer_x_offset=16, pointer_y_offset=18,
                      button_bg=TITLE_MENU_BUTTON, button_x_offset=22, button_y_offset=22, button_gap=12, font_size=18)
    return specs


def get_title_menu():
    data = ['New Game', 'Load Game', 'Settings', 'Acknowledgements', 'Quit']
    logic = [new_game, load_game, goto_settings, goto_acknowledgements, quit_game]
    specs = get_title_menu_specs()
    menu = Menu(data, logic, specs)
    return menu


def title_screen(self):
    self.screen.blit(TITLE_SCREEN_BG, (0, 0))

    text, subtext = get_title_text()
    align_and_blit(self.screen, text, x_ratio=0.5, y_ratio=0.15)
    align_and_blit(self.screen, subtext, x_ratio=0.5, y_ratio=0.28)

    window = self.game.title.menu.blit_options()

    align_and_blit(self.screen, window, x_ratio=0.5, y_ratio=0.75)



