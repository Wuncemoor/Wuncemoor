import pygame as py
import math


def get_surface(image):

    surf = get_alpha_surface(image.get_width(), image.get_height())

    surf.blit(image, (0, 0))
    return surf


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


def get_button_surface(image, text, fontsize, color):
    w, h = image.get_width(), image.get_height()
    surf = get_alpha_surface(w, h)
    text = get_text_surface(text, fontsize, color)
    tw, th = text.get_width(), text.get_height()
    surf.blit(image, (0, 0))
    surf.blit(text, ((w - tw) / 2, ((h - th) / 2) - math.floor(fontsize/5)))

    return surf


def print_message(message_surface, message, off_x, off_y, y):
    fontsize = 12
    text = get_text_surface(message.text, fontsize, color=message.color)

    message_surface.blit(text, (off_x, (y * fontsize) + off_y))


def blit_options(menu, image, off_x, off_y, dy, options, fontsize):

    for i in range(len(options)):
        button = get_button_surface(image, options[i], fontsize, color=(255, 255, 255))
        menu.blit(button, (off_x, off_y + (i * dy)))


def get_offset(screen, text, var):
    if var == 'x':
        return (screen.get_width() / 2) - (text.get_width() / 2)
    elif var == 'y':
        return (screen.get_height() / 2) - (text.get_height() / 2)


def align_and_blit(surface, image, x_ratio=0.5, y_ratio=0.5, x_adjust=0, y_adjust=0):

    off_x = int(surface.get_width() * x_ratio - image.get_width() / 2) + x_adjust
    off_y = int(surface.get_height() * y_ratio - image.get_height() / 2) + y_adjust

    surface.blit(image, (off_x, off_y))

