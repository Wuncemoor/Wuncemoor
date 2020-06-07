import pygame as py


def get_alpha_surface(width, height):
    res_display = py.Surface((width, height))
    ALPHA = py.Color(128, 175, 120)
    res_display.set_colorkey(ALPHA)
    res_display.fill(ALPHA)

    return res_display


def get_text_surface(text, fontsize, color):

    font = py.font.SysFont("comicsansms", fontsize)
    surf = font.render(text, True, color)

    return surf


def print_message(message_surface, message, off_x, off_y, y):
    fontsize = 12
    text = get_text_surface(message.text, fontsize, color=message.color)

    message_surface.blit(text, (off_x, (y * fontsize) + off_y))
