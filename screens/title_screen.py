from pygame.font import Font

from config.image_objects import TITLE_MENU_BG, TITLE_MENU_BUTTON, POINTER_RIGHT
from screens.gui_tools import get_surface, blit_options


def get_title_text():
    tfont = Font('screens\\fonts\\lunchds.ttf', 150)
    stfont = Font('screens\\fonts\\lunchds.ttf', 60)
    text = tfont.render('WUNCEMOOR', True, (0, 0, 0))
    subtext = stfont.render('THE ETERNAL DREAM', True, (0, 0, 0))

    return text, subtext


def get_title_menu(options_current):
    surf = get_surface(TITLE_MENU_BG)
    text = options_current.text
    blit_options(surf, TITLE_MENU_BUTTON, 22, 22, TITLE_MENU_BUTTON.get_height() + 12, text, fontsize=18)
    surf.blit(POINTER_RIGHT, (0, 20 + (options_current.choice * (12 + TITLE_MENU_BUTTON.get_height()))))

    return surf
