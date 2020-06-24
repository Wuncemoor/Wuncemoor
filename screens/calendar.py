from screens.gui_tools import get_surface, get_text_surface, align_and_blit
from config.image_objects import CALENDAR_BG
from config.constants import BLACK


def display_calendar(month, day):

    surf = get_surface(CALENDAR_BG)

    display_month(surf, month)

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
