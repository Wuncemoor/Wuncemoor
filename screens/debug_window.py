import pygame as py
from config.constants import SCREEN_SIZE, WHITE
from screens.gui_tools import get_text_surface, align_and_blit, print_message


def debug_window(self):
    window = py.Surface(SCREEN_SIZE)
    input = get_text_surface(self.handler.current_input, fontsize=30, color=WHITE)
    y = 0
    for message in self.owner.log.debugger.messages:
        print_message(window, message, 0, 0, y)
        y += 1
    align_and_blit(window, input)
    self.screen.blit(window, (0, 0))




