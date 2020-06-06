import pygame as py


def get_alpha_surface(width, height):
    res_display = py.Surface((width, height))
    ALPHA = py.Color(128, 175, 120)
    res_display.set_colorkey(ALPHA)
    res_display.fill(ALPHA)

    return res_display


def get_text_surface(options, i, fontsize):

    font = py.font.SysFont("comicsansms", fontsize)

    surf = font.render(options[i], True, (255, 255, 255))

    return surf
