from config.constants import WHITE
from data_structures.gui_tools import get_text_surface


def split_money(value: int, fontsize: int = 12, color: tuple = WHITE):
    val_str = str(value)

    if value >= 10000:
        gold = get_text_surface(val_str[0], fontsize=fontsize, color=color)
        silver = get_text_surface(cut_leading_zero(val_str[1:3]), fontsize=fontsize, color=color)
        copper = get_text_surface(cut_leading_zero(val_str[3:]), fontsize=fontsize, color=color)

    elif value >= 1000:
        gold = None
        silver = get_text_surface(val_str[0:2], fontsize=fontsize, color=color)
        copper = get_text_surface(cut_leading_zero(val_str[2:]), fontsize=fontsize, color=color)

    elif value >= 100:
        gold = None
        silver = get_text_surface(val_str[0], fontsize=fontsize, color=color)
        copper = get_text_surface(cut_leading_zero(val_str[1:]), fontsize=fontsize, color=color)

    else:
        gold = None
        silver = None
        copper = get_text_surface(val_str, fontsize=fontsize, color=color)

    return gold, silver, copper


def cut_leading_zero(val: str):
    if val[0] == '0':
        return val[1:]
    return val
