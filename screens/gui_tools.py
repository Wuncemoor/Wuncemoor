import pygame as py
import math
from config.constants import BLACK, WHITE


def get_surface(image):

    surf = get_alpha_surface(image.get_width(), image.get_height())
    surf.blit(image, (0, 0))

    return surf


def get_alpha_surface(width, height):

    res_display = py.Surface((width, height), py.SRCALPHA)

    return res_display


def get_text_surface(text, fontsize=12, color=BLACK, style='source_sans_pro'):
    style_dict = {'lunchds': 'fonts\\lunchds.ttf',
                  'gentium': 'fonts\\GentiumBookBasic-Regular.ttf',
                  'source_sans_pro': 'fonts\\SourceSansPro-Regular.ttf',
                  }

    font = py.font.Font(style_dict.get(style), fontsize)
    surf = font.render(text, True, color)

    return surf


def get_button_surface(image, text, fontsize, color, style='source_sans_pro'):

    w, h = image.get_width(), image.get_height()
    surf = get_alpha_surface(w, h)
    text = get_text_surface(text, fontsize, color, style)
    surf.blit(image, (0, 0))
    align_and_blit(surf, text, x_ratio=0.5, y_ratio=0.5, x_adjust=0, y_adjust=math.floor(fontsize/10))

    return surf


def print_message(message_surface, message, off_x, off_y, y):
    fontsize = 12
    text = get_text_surface(message.text, fontsize, color=message.color)

    message_surface.blit(text, (off_x, (y * fontsize) + off_y))


def blit_options(menu, image, off_x, off_y, dy, options, fontsize):

    for i in range(len(options)):
        button = get_button_surface(image, options[i], fontsize, color=WHITE)
        menu.blit(button, (off_x, off_y + (i * dy)))


def align_and_blit(surface, image, x_ratio=0.5, y_ratio=0.5, x_adjust=0, y_adjust=0):

    off_x = int(surface.get_width() * x_ratio - image.get_width() / 2) + x_adjust
    off_y = int(surface.get_height() * y_ratio - image.get_height() / 2) + y_adjust

    surface.blit(image, (off_x, off_y))


def get_wrapped_text(info, width, fontsize, color):
    prewords = info.split()
    words = []
    for word in prewords[:len(prewords)]:
        word += ' '
        words.append(word)
    lines = []
    lines = slice_text(words, lines, width, fontsize)
    surfaces = [get_text_surface(line, fontsize, color) for line in lines]

    return surfaces


def slice_text(words, lines, width, fontsize):

    current_word = 0
    w = 0
    while w < width:
        try:
            maybe = get_text_surface(words[current_word], fontsize)
            w += maybe.get_width()
            current_word += 1
        except IndexError:
            current_word = len(words) + 1
            break
    line = ''
    for i in range(current_word - 1):
        line += words.pop(0)
    lines.append(line)
    if len(words) > 0:
        lines = slice_text(words, lines, width, fontsize)
    return lines

