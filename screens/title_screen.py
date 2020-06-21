import pygame as py

from config.image_objects import TITLE_SCREEN_BG, TITLE_MENU_BG, TITLE_MENU_BUTTON, INDICATOR_H
from screens.gui_tools import get_surface, align_and_blit, blit_options


def title_screen(screen, option):
    screen.blit(TITLE_SCREEN_BG, (0, 0))

    tfont = py.font.Font('screens\\fonts\\lunchds.ttf', 150)
    stfont = py.font.Font('screens\\fonts\\lunchds.ttf', 60)
    titletext = tfont.render('WUNCEMOOR', True, (0, 0, 0))
    tsubt = stfont.render('THE ETERNAL DREAM', True, (0, 0, 0))




    align_and_blit(screen, titletext, x_ratio=0.5, y_ratio=0.25)
    align_and_blit(screen, tsubt, x_ratio=0.5, y_ratio=0.38)
    menu = title_menu(option)
    align_and_blit(screen, menu, x_ratio=0.5, y_ratio=0.75)

def title_menu(option):
    surf = get_surface(TITLE_MENU_BG)
    options = ['Start A New Game', 'Continue Previous Game', 'Quit']
    blit_options(surf, TITLE_MENU_BUTTON, 22, 10, TITLE_MENU_BUTTON.get_height(), options, fontsize=40)
    surf.blit(INDICATOR_H, (0, 10 + (option * TITLE_MENU_BUTTON.get_height())))

    return surf