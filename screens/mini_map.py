import pygame as py
from config.constants import MINI_MAP


def minimap_screen(self):
    (width, height) = MINI_MAP
    (cwidth, cheight) = (1280, 592)

    window = py.Surface((width, height))
    offset_x = 50
    offset_y = 50
    i, j = 0, 0

    for row in self.owner.world.mini:
        for img in row:
            window.blit(img, (offset_x + i, offset_y + j))
            j += 1
        i += 1
        j = 0

    x = cwidth // 2 - width // 2
    y = cheight // 2 - height // 2
    self.screen.blit(window, (x, y))