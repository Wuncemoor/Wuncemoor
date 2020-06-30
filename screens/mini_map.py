import pygame as py

from config.constants import MINI_MAP, CSCREEN
from config.image_objects import MINIMAP


def minimap_screen(screen, world_map):
    (width, height) = MINI_MAP
    (cwidth, cheight) = CSCREEN

    window = py.Surface((width, height))
    offset_x = 50
    offset_y = 50
    i, j = 0, 0

    for row in world_map:
        for tile in row:
            img = MINIMAP.get(tile.type)
            window.blit(img, (offset_x + i, offset_y + j))
            j += 1
        i += 1
        j = 0

    x = cwidth // 2 - width // 2
    y = cheight // 2 - height // 2
    screen.blit(window, (x, y))