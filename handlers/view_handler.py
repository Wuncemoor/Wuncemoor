import pygame as py

from config.image_objects import TITLE_SCREEN_BG, TITLE_MENU_BG, TITLE_MENU_BUTTON, INDICATOR_H
from screens.gui_tools import align_and_blit, get_surface, blit_options


class ViewHandler:
    def __init__(self, screen):
        self.screen = screen
        self.option = 0

    def title_screen(self):
        self.screen.blit(TITLE_SCREEN_BG, (0, 0))

        tfont = py.font.Font('screens\\fonts\\lunchds.ttf', 150)
        stfont = py.font.Font('screens\\fonts\\lunchds.ttf', 60)
        titletext = tfont.render('WUNCEMOOR', True, (0, 0, 0))
        tsubt = stfont.render('THE ETERNAL DREAM', True, (0, 0, 0))

        align_and_blit(self.screen, titletext, x_ratio=0.5, y_ratio=0.25)
        align_and_blit(self.screen, tsubt, x_ratio=0.5, y_ratio=0.38)
        menu = self.title_menu()
        align_and_blit(self.screen, menu, x_ratio=0.5, y_ratio=0.75)

    def title_menu(self):
        surf = get_surface(TITLE_MENU_BG)
        options = ['Start A New Game', 'Continue Previous Game', 'Quit']
        blit_options(surf, TITLE_MENU_BUTTON, 22, 10, TITLE_MENU_BUTTON.get_height(), options, fontsize=40)
        surf.blit(INDICATOR_H, (0, 10 + (self.option * TITLE_MENU_BUTTON.get_height())))

        return surf
