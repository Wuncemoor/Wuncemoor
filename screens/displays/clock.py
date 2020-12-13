import math

from config.constants import BLACK, TWILIGHT_BLUE, MIDNIGHT_BLUE, DARKER_BLUE, DARK_BLUE, MEDIUM_BLUE, STEEL_BLUE, \
    DODGER_BLUE, DARK_CYAN, DEEP_SKY_BLUE, LIGHT_SKY_BLUE, LIGHT_BLUE, LIGHT_CYAN
from config.image_objects import MOON_NEW, MOON_WAXING_CRESCENT, MOON_FIRST_QUARTER, MOON_WAXING_GIBBOUS, MOON_FULL, \
    MOON_WANING_GIBBOUS, MOON_LAST_QUARTER, MOON_WANING_CRESCENT, SUN
from screens.gui_tools import get_alpha_surface, get_text_surface, align_and_blit


def display_clock(time):
    clock = get_alpha_surface(248, 50)

    bg_color = display_clock_bg(clock, time.hour)
    display_celestial_bodies(clock, time)
    display_time(clock, time.hour, bg_color)

    return clock


def display_clock_bg(clock, hour):
    bg_dict = {
        0: BLACK, 1: TWILIGHT_BLUE, 2: MIDNIGHT_BLUE, 3: DARKER_BLUE, 4: DARK_BLUE, 5: MEDIUM_BLUE,
        6: STEEL_BLUE, 7: DODGER_BLUE, 8: DARK_CYAN, 9: DEEP_SKY_BLUE, 10: LIGHT_SKY_BLUE, 11: LIGHT_BLUE,
        12: LIGHT_CYAN, 13: LIGHT_BLUE, 14: LIGHT_SKY_BLUE, 15: DEEP_SKY_BLUE, 16: DARK_CYAN, 17: DODGER_BLUE,
        18: STEEL_BLUE, 19: MEDIUM_BLUE, 20: DARK_BLUE, 21: DARKER_BLUE, 22: MIDNIGHT_BLUE, 23: TWILIGHT_BLUE,
    }
    bg_color = bg_dict.get(hour)
    clock.fill(bg_color)

    return bg_color


def display_celestial_bodies(clock, time):

    moon_dict = {
        0: MOON_NEW, 1: MOON_WAXING_CRESCENT, 2: MOON_FIRST_QUARTER, 3: MOON_WAXING_GIBBOUS, 4: MOON_FULL,
        5: MOON_WANING_GIBBOUS, 6: MOON_LAST_QUARTER, 7: MOON_WANING_CRESCENT
    }

    if 6 < time.hour < 18:
        pass
    else:
        l_moon = moon_dict.get(time.l_moon)
        r_moon = moon_dict.get(math.floor(time.r_moon / 6))
        clock.blit(l_moon, (0, 0))
        clock.blit(r_moon, (200, 0))

    sun_xy_dict = {
        0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: (-24, 34), 7: (-3, 12), 8: (17, 0), 9: (38, -7),
        10: (59, -14), 11: (79, -19), 12: (100, -24), 13: (121, -19), 14: (141, -14), 15: (162, -7), 16: (183, 0),
        17: (203, 12), 18: (224, 34), 19: None, 20: None, 21: None, 22: None, 23: None
    }

    sun_xy = sun_xy_dict.get(time.hour)
    if sun_xy is not None:
        clock.blit(SUN, sun_xy)


def display_time(clock, hour, bg_color):

    if hour < 12:
        xm = 'AM'
    else:
        xm = 'PM'

    if hour == 0:
        hr = '12'
    elif hour < 10:
        hr = '0' + str(hour)
    elif hour < 13:
        hr = str(hour)
    elif hour < 22:
        hr = '0' + str(hour - 12)
    else:
        hr = str(hour - 12)

    tod = get_text_surface(hr + ' : 00 ' + xm, fontsize=20, color=get_negative_color(bg_color))

    align_and_blit(clock, tod, y_ratio=0, y_adjust=38)


def get_negative_color(color):
    r, g, b = color

    neg = (255 - r, 255 - g, 255 - b)
    return neg
