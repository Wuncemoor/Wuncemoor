from screens.gui_tools import get_surface, get_text_surface, align_and_blit
from config.image_objects import CALENDAR_BG, CALENDAR_CIRCLE
from config.constants import BLACK


def display_calendar(time):

    surf = get_surface(CALENDAR_BG)

    display_month(surf, time.month)
    display_day(surf, time.day)

    return surf

def display_month(surf, month):

    dict = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'july',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December',

    }

    month = get_text_surface(dict.get(month), fontsize=32, color=BLACK)
    align_and_blit(surf, month, x_ratio=0.5, y_ratio=0, x_adjust=0, y_adjust=20)


def display_day(surf, day):

    dict = {
        1: (0, 0), 2: (1, 0), 3: (2, 0), 4: (3, 0), 5: (4, 0), 6: (5, 0),
        7: (0, 1), 8: (1, 1), 9: (2, 1), 10: (3, 1), 11: (4, 1), 12: (5, 1),
        13: (0, 2), 14: (1, 2), 15: (2, 2), 16: (3, 2), 17: (4, 2), 18: (5, 2),
        19: (0, 3), 20: (1, 3), 21: (2, 3), 22: (3, 3), 23: (4, 3), 24: (5, 3),
        25: (0, 4), 26: (1, 4), 27: (2, 4), 28: (3, 4), 29: (4, 4), 30: (5, 4),
    }

    (x, y) = dict.get(day)
    align_and_blit(surf, CALENDAR_CIRCLE, x_ratio=0, y_ratio=0, x_adjust=(25 + 30 * x),
                   y_adjust=(75 + 18 * y))
